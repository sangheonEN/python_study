# 조건에 부합하는 한 특정한 명령어를 반복
# 숫자 범위 표현 : range(시작, 끝)
# range(1, 20) 1 ~ 19 까지의 수 표현 범위 : 시작 ~ 끝-1

# range() 사용 법
# sum = 0
# for i in range(1, 10):
#     # print(i)
#     sum = sum + i
#     print(sum)
# print("합계 : ", sum)

# 문자열 처리
# count = 0
# for i in "Hello World":
#     if i == 'o':
#         count = count + 1
# print("o의 갯수는 ", count, "개 입니다.")

# # 리스트 처리
# sum = 0
# list = [10, 21, 39, 40, 50]
# for i in list:
#     if i % 2 == 1:
#         # print(i)
#         continue
#     if i == 50:
#         # print(i)
#         break
#     print(i)

# 리스트 원소 출력하기 (for문)
# numbers = [1, 2, 3, 4, 5]
# for i in range(5):
#     number = numbers[i]
#     if number % 2 == 0:
#         print("짝수이고 number : ", number)
#     else:
#         print("홀수이고 number : ", number)
#
# try:
#     position = 0
#     while position < 5:
#         number2 = numbers[position]
#         if number2 % 2 == 0:
#             print("짝수이고 number : ", number2)
#             position += 1
#         else:
#             print("홀수이고 number : ", number2)
#             position += 1
# except Exception as e:
#     print(e)

# 문자열 출력
# word = 'trud'
# print("trud 문자열 길이 :", len(word))
# offset = 0
#
# while offset < len(word):
#     print(word[offset])
#     offset += 1
#
# for letter in word:
#     print(letter)

# # continue 사용하기
# print("continue, break 사용")
# while True:
#     try:
#         value = input("문자를 입력하시오. ")
#         if value == 'end':
#             print("종료")
#             break
#         number = int(value)
#         if number % 2 == 0:
#             print("짝수는 출력 안한다!")
#             continue
#         else:
#             print("홀수 : ", value)
#     except Exception as e:
#         print(e)

# for과 in으로 순회하기.
# 이터레이터는 유용하게 자주 쓰인다.




