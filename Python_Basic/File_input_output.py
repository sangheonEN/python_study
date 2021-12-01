# # 읽어오고 싶은 file과 동일한 위치에 있으면 바로 읽어올 수 있음.
#
# # open("파일명", "r or w", encoding="UTF-8") : 파일을 특정한 모드로 여는 함수. 읽을 때는 r, 쓸 때는 w. encoding="UTF-8" 유니코드화
# f = open("input.txt", "r", encoding="UTF-8")
# # seek() : 몇 번째 byte 부터 읽을까? 파이썬 : 한 글자마다 3byte로 인식
# f.seek(9)
# # read() : 파일 객체로부터 모든 내용을 읽는다.
# data = f.read()
# print(data)
# # close() : 해당 파일을 모두 읽었거나 모든 행위를 끝났을 때는 close 함수로 닫아줘야함. 즉, 해당 파일에 대한 리소스 작업을 모두 끝났다는 걸 알림.
# f.close()
#
# print("\n")
#
# # readline() : 반복문을 사용해서 한줄씩 읽을 수 있게
# g = open("input.txt", "r", encoding="UTF-8")
# count = 0
# while count < 3:
#     data1 = g.readline()
#     count += 1
#     print("%d번째 줄 문자열 : %s" %(count, data1), end="ㅋㅋ") # end="" 1단계가 끝나는 반복문일때 마지막에 붙여주는 어떤 문자열을 넣고 싶을 때
# g.close()
#
# print("\n")
#
# # readlines() : 전체 내용을 한 번에 리스트에 담는 함수
# h = open("input.txt", "r", encoding="UTF-8")
# data2 = h.readlines()
# print(data2)
# h.close()
#
# print("\n")
#
# # readlines() : 리스트에 담은 것을 enumerate() 함수를 이용해 인덱스를 한줄로 생각하고 그 줄에 맞는 문자열을 출력해보자.
# t = open("input.txt", "r", encoding="UTF-8")
# list = t.readlines()
# for i, data in enumerate(list):
#     print("%d줄 : %s" %(i+1, data), end="") # 기본적으로 print() 끝날때마다 개행이 이루어 지는데 end=""으로 개행을 없애줌
# t.close()
#
# print("\n")
#
# # with : file을 불러오는 명령구문을 어떤 하나의 명칭으로 정의할 수 있다. 그리고, close()함수 없이 자동으로 작업이 끝나면 리소스 작업을 끝낸다. 즉, open(), close()를 생략가능
# with open("input.txt", "r", encoding="UTF-8") as d:
#     list2 = d.readlines()
#     for l, data3 in enumerate(list2):
#         print("%d줄 : %s" %(l+1,data3), end="")


# # 파일에 포함된 문자의 빈도수를 출력하는 예제
# def function(str):
#     with open(str, "r") as z:
#         # 키 : 알파벳, 값 : 빈도수
#         dict = {}
#         list3 = z.read()
#         for i in list3:
#             if i in dict:
#                 dict[i] += 1
#             else:
#                 dict[i] = 1
#     return dict
# dict = function("input_2.txt")
# print(dict)
# dict = sorted(dict.items(), key=lambda a:a[1], reverse=True)
# print(dict)
# for data, count in dict:
#     if data == " " or data =="\n":           # 줄 바꿈이나 " " 공백은 무시하고 출력!
#         continue
#     else:
#         print("값 : %c, 빈도수 : %d\n" %(data, count), end="")

