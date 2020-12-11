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

# 리스트 처리
sum = 0
list = [10, 21, 39, 40, 50]
for i in list:
    if i % 2 == 1:
        # print(i)
        continue
    if i == 50:
        # print(i)
        break
    print(i)