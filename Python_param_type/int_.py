# 숫자 자료형
# A = 10
# B = 20.123 # 정수를 포함하는 실수 기준으로 형변환되어 연산됨
# print(A+B)
# C = "DFASD"
# # print(A+B+C)
# C1 = int("1243")
# print(A+B+C1)

# int() 정수형 변환
a = "123"
print(int(a))

# 16 진수 처리 F = 15
# a = 0xFFFF # FFFF 4자리수 각 자리수가 4BIT 총 16BIT로 표현할 수 있는 가능 큰 숫자를 출력
# a1 = 0xFFFFF
# a_1 = 0x0000001
# a_10 = 0x0000010
# a_100 = 0x0000100
# a_1000 = 0x0001000
# print(a)
# print(a1)
# print(a_1) #16 0승
# print(a_10) #16 1승
# print(a_100) #16 2승
# print(a_1000) #16 3승

# 4칙연산       // 몫 연산. 그리고 int(32비트 -2,147,483,648~ 2,147,483,647), long(32비트 -2,147,483,648~ 2,147,483,647), long long(64비트 -9,223,372,036,854,775,808~ 9,223,372,036,854,775,807) 등 표현할 수 있는 숫자 크기가 제한되어 있지 않음
a = 602
b = 20
print("a = {}, b = {}".format(a, b))
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b) # 나누기됨!
print("a // b = ", a // b) # 단순히 몫만 계산하기 위해
print("a % b = ", a % b)

# 복소수 연산 가능. 선형대 수학에서 유용하게 활용
# a = (1+2j)
# b = (3+4j)
# print(a*b)

