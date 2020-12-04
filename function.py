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

# 가변인자 : 함수의 매개변수가 가변할 수 있을 때 사용   표현법 : *변수명, 출력 : 튜플 형태로 출력
# def function(*data):
#     print(data)
# function(1, 2, 3)

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



