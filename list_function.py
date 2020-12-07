# index(원소) 리스트내 특정한 원소의 인덱스를 찾는 함수
# list = ['ads', 'sdf', 'a', 'sadsaf', 'dddd']
# print(list.index('a'))
# list.reverse()
# print(list)
# list2 = list[::-1] # step 매개변수에 -1을 넣어줘야 reverse
# print(list2)

# sum() 문자열 원소는 연산이 안됨
# list3 = [1, 2, 3, 0.24]
# print(sum(list3))

# # range(시작, 끝) : 특정 범위를 지정
# # list(특정 범위) : range(시작, 끝) 시작 ~ 끝 - 1의 수까지 만 범위의 리스트를 만듬
# my_range = range(5, 10)
# list4 = list(my_range)
# print(list4)

# # all() : 모든 원소가 참인지 판별 / any() 원소 중 하나라도 참인지 판별
# list5 = [True, False, True]
# print(all(list5), any(list5))
#
# # enumerate() : 리스트에서 원소와 인덱스를 함께 추출할 수 있음.
# list6 = ["24", "26235", "1235", "436436"]
# a = enumerate(list6)                          # 리스트 원소를 enumerate화 시킨다.
# b = list(enumerate(list6))                    # 다시 리스트 함수로 각 원소들을 묶는다.
# print(a)
# print(b)                                      # 튜플 형식으로 (인덱스, 원소)출력됨.
# # enumerate() for 문 활용
# for e, f in enumerate(list6):
#     print("인덱스 :", e, "원소 :", f)
#
# # sort() : 리스트의 원소 정렬
# list7 = ["이상헌", "김도겸", "김세인", "박동건"]
# list7.sort()
# print(list7)
#
# # count() : 리스트 특정한 원소의 개수 추출
# print(list7.count("이상헌"))
#
# # del() : 리스트 특정한 원소를 삭제, insert(인덱스, 넣고자하는 값), append() 가장 마지막 인덱스에 원소를 넣음
# list8 = [1, 2, 3, 4, 5]
# del list8[1:3]
# print(list8)
# list8.insert(2, -1002)
# print(list8)
# list8.append(12394)
# print(list8)
#
