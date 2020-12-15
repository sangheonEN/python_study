# 설탕을 정확하게 N킬로그램 배달
#
# 봉지는 3킬로그램 봉지와 5킬로그램 봉지
#
# 최대한 적은 봉지
#
# 18kg 배달 시
# 3kg :  6봉 배달
# 5kg 3봉, 3kg 1봉 배달
#
# 더 적은 개수의 봉지 배달 가능
#
# 1. 5kg 먼저 봉지하고 3kg을 봉지한다.
#
# 1. 5kg 먼저 봉지하고 3kg을 봉지한다.
#
# 1. 5kg 먼저 봉지하고 3kg을 봉지한다.
#
# - N을 5로 나누었을 때 나누어 떨어지는 몫
#
# - N을 3으로 나누었을 때 나누어 떨어지는 몫
#
# - N을 8로 나누었을 때 나누어 떨어지는 몫 * 2 + 그 몫에 3 or 5로 나누어 떨어지는 몫

# 2839 설탕 배달
N = int(input())
box = 0
while True:
    if N % 5 and N >= 3 == 0:
        box += N // 5
        print(box)
    N -= 3
    box += 1
else:
    print(-1)






























# 삽질
# a = int(input())
# print(a)
#
# a5 = 0
# a3 = 0
# a8_RR = 0
# result = 0
# if a >= 3:
#     if a % 5 == 0:
#         result = a // 5
#     if a % 3 == 0:
#         result = a // 3
#     if a % 8 != 0:
#         a8 = a % 8
#         a8_R = 2 * (a // 8)
#         if a8 % 3 == 0:
#             a8_3 = a8 // 3
#             result = a8_R + a8_3
#         elif a8 % 5 == 0:
#             a8_5 = a8 // 5
#             result = a8_R + a8_5
#         else:
#             print(-1)
#     if a % 8 == 0:
#         result = 2 * (a // 8)
# else:
#     print(-1)
# print(result)

