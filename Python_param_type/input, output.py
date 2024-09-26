# 변수에게 사용자가 사용할 값을 전달함
a = input()
print(a)

# 띄어 쓰기로 입력 받을 때 split 함수 사용.
# 배열 형태로 반환되니까 input 받은 데이터는 문자열 형태로 가지고 있으니 나누기 위해서
# 문자열 자체를 ' ' 공백을 기준으로 나누겠다.
a = input().split(" ")
# a = ['3', '7'] 3 7 입력하면 a에다가 공백을 기준으로 나누어져서 배열의 원소로 들어감
x = int(a[0])
y = int(a[1])
print("x + y = ", x + y)
print("x - y = ", x - y)
print("x * y = ", x * y)
print("x / y = ", x / y)
print("x // y = ", x // y)
print("x % y = ", x % y)

a = input().split(' ')
x = int(a[0])
y = int(a[1])
print(x + y)

None
b = None # NULL과 같다
print(b)
print(x + b)  # None 이라는 것은 실제로 소스코드에서  b = None라고 b를 정의하면 b 변수의 메모리 공간이 어떠한 것도 가르키지 않는 상태인 것을 나타 냄
