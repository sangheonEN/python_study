# # 6.1번
# alist = [3, 2, 1, 0]
# for i in alist:
#     print("alist = {}".format(i))

# # 6.2번
# guess_me, number = map(int, input().split())
#
# while True:
#     if guess_me > number:
#         print("too low")
#         # print("guess_me = {}".format(guess_me))
#         number += 1
#     elif guess_me == number:
#         print("found it!")
#         # print("동점")
#         number += 1
#     else:
#         print("oops")
#         # print("number = {}".format(number))
#         break

# # 6.3번
# print("guess_me 입력 : ")
# guess_me = int(input())
# for number in range(0, 10):
#     if number < guess_me:
#         print("too low")
#     elif number == guess_me:
#         print("found it!")
#     else:
#         print("oops")
#         break