# a = 10
# b = 20
# print(a+b)
#
# INPUT 함수
# c = input("데이터를 넣어 주세요.") # scanf()
# print(c)

# A = input("A : ")
# B = input("B : ")
# # print는 기본적으로 개행이 된다 하지만, 마지막에 , end=''을 붙이면 ''빈공간이 만나면 만나면 끝나게됨
# print("A+B = ", end='')
# print(int(A) + int(B))

# CASE 1
# 전역변수 : a 지역변수 : b,c
# a = 10
# print("데이터를 입력하시오.", end="")
# d = input()
# def func(b):
#     c = a + b
#     return c
# print(func(int(d)))

# CASE 2
# a = 10
# print('데이터를 입력하시오.')
# def A(b, c):
#     d = a+b+c
#     return d
# def Square():
#     b = a*a
#     return b
# C = 10* Square()
# print(A(20, 30))
# print(C)

# def go():
#     print("Hello")
#     print("Hello")
#     print("Hello")
# print(go(), end='')
# print(go(), end='')
# print(go(), end='')


# ADD 사용자 정의 함수 만들기 OR 함수 안에서 PRINT() 하기
# a = int(input())
# b = int(input())
#
# def add(a, b):
#     c = a + b
#     return c
# def minus(a, b):
#     c = a - b
#     return c
#
# print(add(a, b))
# print(minus(a, b))

# 단순 조건문
# a = int(input())
# def A(a):
#     b = 20
#     c = a+b
#     return c
# if A(a)>=40:
#     print(A(a))
# else:
#     print("총합이 40이 넘지 않았습니다.")

# 문자열 연산 및 개요
# print("안녕 \"클레오\" 파트라~ 세상에서 \t제일 가\n는 포테\n이토 칩!")
# a = "이dd"
# b = "뭐 dd"
# print((a + b+"\t") * 5)

# 문자열 인덱싱 및 슬라이스 기법
# a = "Hello World"
# print((a[0]+a[3]))
# print(a[-1])
# print(a[2:3])
# print(a[2:4])
# print(a[2:5])
# print(a[2:6])
# print(a[2:7])
# print(a[:-2])
# print(a[0:-2])
# print(a[1:-2])
# print(a[:])
# print(a[0:7:2]) # 0~7인덱스 까지 2씩 올라가면서 출력 a[0], a[2], a[4], a[6]















