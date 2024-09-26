# # input() 사용자로부터 입력 받는 함수. 문자열로 처리됨
# # int() 정수형으로 변환
# # float() 문자열, 정수 자료형 등을 실수형으로 변환
# user_input = int(input("정수를 입력하시오 : "))
# print("입력 값 :", user_input)
# print("제곱 :", user_input ** 2)
# a = 10
# print(float(a))

# max(), min()
list = [5, 23, 19, 10, 3, 4, 7, 100, 20]
print(max(list), min(list))

# bin() : 10진수 -> 2진수 변환, hex() 10진수 -> 16진수로 변환. 반환 값은 문자열!
print("10진수 -> 2진수 변환 bin(128) :", bin(128), "10진수 -> 16진수로 변환 hex(128) :", hex(128))
# 16진수 -> 10진수로 변환 int()
print("16진수 -> 10진수 변환 int(\'0xe6\', 16) :", int('0xe6', 16))
# 2진수 -> 10진수로 변환 int()
print("2진수 -> 10진수 변환 int(\'0b10001\', 2) :", int('0b10001', 2))

# round() 반올림 함수
print(round(123.12412, 2), round(123.1234, -1))

# type() 자료형 종류 출력
int = 1
str = '문자열'
list = [1, 2, 3]
dict = {"bbxc", "asdg", "213"}
print(type(int))
print(type(str))
print(type(list))
print(type(dict))



