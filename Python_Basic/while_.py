# # 특정한 조건을 만족할때만 소스코드를 반복적으로 수행
# i = 0
# sum = 0
# while i <= 5:
#     i = i+1
#     if i % 2 == 1:
#         continue
#     sum = sum + i
# print("합계 : ", sum)

# count = 1
# while count <= 5:
#     print("count = {}".format(count))
#     count += 1

# # break문 활용
# while True:
#     a = input("문자를 입력하시오.")
#     if a == '0':
#         break
#     else:
#         print("0이 아닌 수 {}".format(a))

# continue문 활용
count = 0
while count <= 5:
    count += 1
    if count == 3:
        continue
    else:
        print(f"count = {count}")

# 문자열 순회 출력
word = 'tufud'
offset = 0
while offset < len(word):
    print(f"word = {word[offset]}")
    offset += 1