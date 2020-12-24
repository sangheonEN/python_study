# 함수 input -> process -> output
# 함수를 이용하면 특정한 소스코드를 줄일 수 있다.
# a = input().split(" ")
# def add(a):
#     sum = int(a[0]) + int(a[1])
#     return sum
# print(add(a))
#
# def add2(a, b):
#     print(a + b)
# add2(10, 20)

# # 함수를 매개변수로 받아 들일 수 있나?
# def a():
#     print("전달 되었나?")
# def c(a):
#     print("전달 받았다!")
# c(a())

# 가변인자 : 함수의 매개변수가 가변할 수 있을 때 사용   표현법 : *변수명, 출력 : 튜플 형태로 출력
# def function(*data):
#     print(data)
# function(1, 2, 3)

# 가변 매개변수. def aaa(a, b, *c) *c 더 들어올 수 있게 하기 위해 *를 적어줌.
# def aaa(a, b, *c):
#     print("a = {}".format(a))
#     print("b = {}".format(b))
#     print(c)
#     for cstr in c:
#         print("c = {}".format(cstr))
# aaa(10, 20, 30, 40, 50)

# 함수안에서 전역변수 선언하기
# def add3():
#     global a # 전역 변수 사용
#     a += 5
# a = 2        # a = 2
# add3()       # a+= 5 -> a = 7
# print(a)

# 반환 값이 여러개일 수 있다. 튜플 형태로 반환된다.
# def function():
#     a = 5
#     b = [1, 2, 3]
#     return a, b
# a, b = function()
# print(a)
# print(b)

# # None과 False는 다르다. # 0, 0.0, 빈문자열, 빈리스트, 빈튜플, 빈 딕셔너리... 등등 은 모두 False이며, None이 아니다.
# # def doA():
# #     return
# # if doA() is None:
# #     print("None인가?")
# # else:
# #     print("None이 아닌가?")
#
# def which(a):
#     if a is None:
#         print(f"{a} is None")
#     elif a:
#         print(f"{a} is True")
#     else:
#         print(f"{a} is False")
#
# print(which([0]))           # 원하는 값을 넣어서 None인지 True인지 False인지 확인해보자.
#
# # 위치 인수 : 값을 순서대로 상응하는 매개변수에 복사하는 것.
#
# def menu(a, b, c):
#     return {'wine' : a, 'bottle' : b, 'combine' : c}
# print(menu('cherry wine', 'two bottle', 'c?'))

# # global 변수 사용
# a = 10
# def doA():
#     b = 20
#     global a = 20
#     print(a)
#     print(f"a+b = {a+b}")
# doA()

# # 독스트링
# def doB():
#     '''this is doA function'''
#     return 'a'
# print(doB)               # 주소값
# print(doB())             # return
# print(doB.__doc__)       # 독스트링 작성 내용 출력
# print(doB.__name__)      # 함수 이름
# print(type(doB))         # type은 class이며, class가 정의 하는 것은 function이다.
# print(type(doB()))

# # 내부 함수(함수안에 함수를 넣을 수 있음.)
# def outer(a, b):
#     def inner(c, d):
#         return c+d
#     return inner(a, b)
# print(outer(4, 7))



# 클로저


# # 제너레이터 함수 : 순회되고 메모리에서 삭제됨. 시퀀스를 생성하는 객체라고 생각해야함. 그래서 보통 이터레이터에 많이 사용됨.
# # 대표적으로 range() 함수를 제너레이터 함수로 자주 사용함.
# # yield와 return의 차이 return은 반환하고 함수를 끝내버림. yield는 반환 하고 계속 진행함.
# def mp_range(first = 0, last = 10, step = 1):
#     number = first
#     while number < last:
#         yield number
#         number += step
# range = mp_range(1, 5)
# print(range)
#
# for x in range:
#     print(x)
# print("다시 출력") # 제너레이터 함수로서 메모리에서 삭제됨. 출력이 되는 순간.
# for x in range:
#     print(x)

# # 제너레이터 컴프리핸션
# gene = (number for number in zip([1, 2], [3, 4]))
# for x in gene:
#     print(x)
# print("다시 출력")
# for x in gene:
#     print(x)

# 데커레이터 : 하나의 함수를 취해서 또 다른 함수를 반환하는 함수
# 1. 함수 이름과 인수를 출력하는 함수
# 2. 인수로 함수를 실행하는 함수
# 3. 결과를 출력하는 함수
# 4. 수정된 함수를 사용하도록 반환한다.
def document_it(func):
    def new_function(*args, **kwargs):
        print(f"1번 함수. 함수 이름과 인수를 출력. 이름 : {func.__name__}, 인수 : {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result : {result}")
        return result
    return new_function












