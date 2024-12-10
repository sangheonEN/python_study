"""
Python에서는 모든 것이 객체로 존재한다. Cpython을 보면, PyObject이 명칭의 구조체로 C코드로 구현되어 있더라. 그래서, int, float과 같은 data type부터 list, dict 등과 같은 자료형, Class, def 까지 모두 다 PyObject를 기반으로 한다.

그리고 PyObject들은 private Heap 공간에 할당된다. [3]

만약에 정수 100을 저장하는 a 변수를 선언하고, a를 b에 대입한 뒤 a = a + 1을 하게 되면, a가 가르키고 있던 정수 100에 대한 heap 메모리를 삭제하고 정수 101로 할당한다. 그리고 b는 계속 정수 100에 대한 heap 메모리 주소를 가르킨다.
a = 100
b = a
a = a + 1

결국, 값이 증가하거나 낮아지면, 기존의 값의 heap 메모리는 free되고 새로운 값의 heap 메모리가 malloc되고 거기를 변수가 가르키게 된다. [4]

이 private Heap은 Python 프로세스의 전용 메모리 영역이며 모든 객체 및 데이터는 여기에 저장된다.

malloc과 free를 자주 호출하면, 레이턴시가 커진다. 이를 방지 하기 위해서 할당자에 대한 계층 구조를 정의해서 메모리를 관리한다. 

가장 하위 계층 부터 general-purpose allocator, raw memory allocator, Object allocator, specific memory로 구성된다.

General Purpose Allocator (CPython 의 malloc 메서드): 메모리 계층 구조의 가장 아래에는 General Purpose Allocator 가 있다. 범용 할당자는 CPython 용 `C 언어의 malloc` 메서드이다. 이는 운영 체제의 가상 메모리 관리자와 상호작용하여 Python 프로세스에 필요한 메모리를 할당한다. 또한, 운영체제의 가상 메모리 관리자와 통신하는 유일한 할당자이다. 
Raw memory Allocator (512 byte 보다 큰 객체용): General Purpose Allocator 위에는 Python 의  Raw memory Allocator 가 있다. Raw memory Allocator 는 General Purpose Allocator(=malloc) 에 대한 추상화를 제공한다. Python 프로세스에 메모리가 필요한 경우, Raw memory Allocator 는 General Purpose Allocator 와 상호작용하여 필요한 메모리를 제공한다. 그리고 Python 프로세스의 모든 데이터를 저장할 충분한 메모리 공간이 있는지 확인한다. 
Object Allocator (512 byte 보다 작거나 같은 객체용): Raw memory Allocator 위에는 Object Allocator 가 있는데, 이 할당자는 512 byte 이하의 작은 객체에 대한 메모리 할당에 사용된다. 만약 객체에 512 byte 이상의 메모리가 필요한 경우 Python 의 메모리 관리자는 Raw memory Allocator 를 직접 호출한다.
Object-specific Allocators (특정 데이터 유형에 대한 특정 메모리 할당자): Object Allocator 위에는 Object-specific Allocators 가 있다. 정수, 실수, 문자열 및 리스트와 같은 단순 데이터 유형에는 각각의 객체별 할당자가 있다. 이러한 객체별 할당자는 객체의 요구 사항에 따라 메모리 관리 정책을 구현한다. 즉, 정수에 대한 객체별 할당자는 실수에 대한 객체별 할당자와 구현 방식이 다르다.
Object Allocator 와 Object-specific Allocators 모두 Raw memory Allocator 에 의해 Python 프로세스에 이미 할당된 메모리에서 작동한다. 이러한 할당자는 운영 체제에서 메모리를 직접 요청하지 않고, 프라이빗 힙에서 작동한다. Object Allocator 와 Object-specific Allocators 에 더 많은 메모리가 필요한 경우 Python 의 Raw memory Allocator 가 General Purpose Allocator 와 상호작용하여 메모리를 제공한다.

여기서 중요한 부분은 Object Allocator에 대한 이해다.

Object Allocator(pymalloc): 요청된 객체 메모리 크기가 512 byte 미만일 때, Object Allocator 를 사용하여 할당한다. [4] 

1. 512 byte 미만 객체가 메모리를 요청하면 해당 객체에 대한 메모리를 할당하는 대신, 객체 할당자가 운영체제에서 큰 메모리 블록을 요청.

2. 객체 할당자가 할당하는 큰 메모리 블록을 Arena라 명명하고, Arena 의 크기는 256KB이다.

3. Arena 를 효율적으로 사용하기 위해서 CPython 은 Arena 를 Pool(4KB) 로 나눈다. 따라서 Arena 는 64개의 Pool 로 구성된다.

4. Pool 은 다시 Block으로 나뉜다.

5. Block은 object allocator 가 객체에 할당할 수 있는 가장 작은 메모리 단위이다.

6. Block은 하나의 객체에만 할당될 수 있고, 객체 또한 하나의 Block에만 할당될 수 있다.

7. 블록은 다양한 크기로 제공된다. 블록의 최소 크기는 8 byte 이고, 최대 크기는 512 byte 이다. 블록 크기는 8의 배수로 8, 16, 24, 32, ..., 504, 512 byte가 될 수 있다.

이러한 내용을 안다면, 향후에 어떤 메모리 구조에 접근해서 데이터가 저장되는지 파악할 수 있기 때문에 메모리 구조를 보다 깊게 파악할 수 있다고 생각한다.


garbage collection(gc)이란 Python 프로그램에서 생성된 객체가 더 이상 프로그램에서 접근할 수 없거나 필요하지 않은 객체를 메모리에서 수거하는 역할을 한다.

- 여기서 정의하는 필요하지 않은 객체란? 참조 카운트가 0인 객체 또는 순환 참조로 인해 참조 카운트가 0이 되진 않았지만, 사용 불가능한 객체이다.

- 참조 카운트가 0인 객체는 특정하기 쉬워 수거가 용이하다.

- 순환 참조 문제란? 자기 자신을 참조하거나 서로 다른 두 객체가 서로를 참조하여, 가비지 컬렉션 대상에 포함되지 않아 해당 객체들이 불필요해져도 메모리 회수되지 않는 문제 [2]

- python에서는 gc.collect()를 활용하면, 순환 참조 문제까지 자동으로 해결할 수 있다.

- gc.collect(generation: int = 2) 최대 2세대까지 있고 각 세대에 대한 설명은 이와 같습니다.


Reference
[1] https://docs.python.org/ko/3.12/library/gc.html#module-gc
[2] https://velog.io/@jshong0907/Python-Garbage-Collection
[3] https://docs.python.org/ko/3.13/c-api/memory.html
[4] https://sysgongbu.tistory.com/208

"""

import sys
import gc

def circular_reference():
    """
    순환 참조를 모방한 코드
    
    """
    
    
    
    # 순환 참조 생성
    class Node:
        def __init__(self, next_link=None):
            self.next_link = next_link

    node_3 = Node()
    node_2 = Node(node_3)
    node_1 = Node(node_2)
    node_3.next_link = node_1
    A = node_1
    
    print("del 이전 node_3 참조 카운트:", sys.getrefcount(node_3))
    print("del 이전 node_2 참조 카운트:", sys.getrefcount(node_2))
    print("del 이전 node_1 참조 카운트:", sys.getrefcount(node_1))
    print("del 이전 A 참조 카운트:", sys.getrefcount(A))

    # 객체 삭제
    # del node_1, node_2, node_3
    
    # 이렇게 del을 적용한 객체는 사용할 수 없어서 print가 찍히지 않음.
    # 오류 구문: UnboundLocalError: cannot access local variable 'node1' where it is not associated with a value
    # print("del 이후 node1 참조 카운트:", sys.getrefcount(node1))
    # print("del 이후 node2 참조 카운트:", sys.getrefcount(node2))


    # 이 시점에서 참조 카운트는 0이 아니지만, 프로그램에서는 접근할 방법이 없음
    # gc.set_debug(gc.DEBUG_LEAK)
    print("수거 전 gc.garbage:", gc.garbage)
    print("수거 전 gc.get_count():\n", gc.get_count())
    print(f"수거 전 gc.collect(): {gc.collect()}")  
    print(f"수거 전 gc.get_objects(generation=0): {gc.get_objects(generation=0)}")  
    print(f"수거 전 gc.get_objects(generation=1): {gc.get_objects(generation=1)}")  
    print(f"수거 전 gc.get_objects(generation=2): {gc.get_objects(generation=2)}")  
    gc.collect()
    print("수거 후 gc.garbage:", gc.garbage)
    print("수거 후 gc.get_count():", gc.get_count())
    print(f"수거 후 gc.collect(): {gc.collect()}")
    print(f"수거 후 gc.get_objects(generation=0): {gc.get_objects(generation=0)}")
    print(f"수거 후 gc.get_objects(generation=1): {gc.get_objects(generation=1)}")
    print(f"수거 후 gc.get_objects(generation=2): {gc.get_objects(generation=2)}")


def reference_cnt():
    """
    - 출력 결과 -

    참조 카운트: 2
    참조 카운트: 3
    참조 카운트: 2

    """
    
    k = "abc"
    print(f"k : {k}")
    print(f"k = str(abc) 참조 카운트:{sys.getrefcount(k)}")
    print("Python 버전:", sys.version)
    print(gc.get_referrers(k))

    
    # a = [1, 2, 3]  # 리스트 객체 생성
    # print("참조 카운트:", sys.getrefcount(a))  # 참조 카운트 확인 (내부적으로 gc도 참조하므로 1 이상)

    # b = a           # `b`가 `a`를 참조
    # print("참조 카운트:", sys.getrefcount(a))  # 참조 카운트 증가

    # del b           # `b` 참조 삭제
    # print("참조 카운트:", sys.getrefcount(a))  # 참조 카운트 감소


if __name__ == "__main__":
    
    reference_cnt()
    
    # circular_reference()