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

# # sort() : 리스트의 원소 정렬(내부적으로)
# list7 = ["이상헌", "김도겸", "김세인", "박동건"]
# list7.sort()
# print(list7)

# # sorted() : 리스트의 정렬된 복사본을 반환하니까 타 변수에 할당해서 출력
# list7 = ["이상헌", "김도겸", "김세인", "박동건"]
# sorted_list7 = sorted(list7)
# print(list7)
# print(sorted_list7)

# # count() : 리스트 특정한 원소의 개수 추출
# print(list7.count("이상헌"))
#
# # del() : 리스트 특정한 원소를 삭제
# list8 = [1, 2, 3, 4, 5]
# del list8[1:3]
# print(list8)
# list8.insert(2, -1002)
# print(list8)
# list8.append(12394)
# print(list8)

# # insert(인덱스, 넣고자하는 값) 오프셋과 insert()로 항목 추가하기
# marxeo = ['Groucho', 'Chico', 'Harpo']
# marxeo.insert(0, "ㅍㄴㅁ") # 오프셋 0은 맨 처음 인덱스에 원소를 넣어줌
# marxeo.insert(2, "aaa") # Chico 1번 index와 Harpo 2번 index 사이
# marxeo.insert(100, "ddd") # 최대 index를 초과해도 맨 끝으로 넣어줌.
# print(marxeo)
#
# # append() 가장 마지막 인덱스에 원소를 넣음
# marxeo2 = ['Groucho', 'Chico', 'Harpo']
# marxeo2.append("dff")
# print(marxeo2)

# # split(나누는 기준) 나누어서 list 원소로 변환
# datee = '2020/10/30'
# print(datee.split("/"))

# # list 병합 extend() 사용
# alist = ["1", "2", "3", "4"]
# blist = ['23', "34", "45", "56"]
# alist.extend(blist)
# print(alist)
# # list 병합 += 사용
# clist = ["1", "2", "3", "4"]
# dlist = ['23', "34", "45", "56"]
# clist += dlist
# print(clist)
# # append() 는 병합하지 않고 list채로 그대로 맨 끝 인덱스에 삽입
# elist = ["1", "2", "3", "4"]
# flist = ['23', "34", "45", "56"]
# elist.append(flist)
# print(elist)

# # remove()
# blist = ['23', "34", "45", "56"]
# blist.remove('23')
# print(blist)

# # pop() : 리스트에서 항목을 가져오는 동시에 그 항목을 삭제함. 맨 끝 index 원소를 가져감.
# # 선입선출 = 자료구조 queue 구현 이나 후입선출 = 자료구조 stack 구현 할 수 있음.
# clist = ['123', '124', "125", "126"]
# print(clist.pop())
# print(clist)
# print(clist.pop(0))
# print(clist)
# print(clist.pop(1))
# print(clist)

# # clear() 모든 항목 지움
# tlist = [10, 20, 30, 40]
# tlist.clear()
# print(tlist)

# # index() 값으로 오프셋 찾기!
# tlist = [10, 20, 30, 40]
# print(tlist.index(20))
#
# # in() 리스트 원소 존재여부 확인
# tlist = [10, 20, 30, 40]
# print(10 in tlist)

# count() 특정 원소가 몇 개 들어 있냐?

# len() 전체 원소 개수 출력

# join()

# # copy() : list 복사, 슬라이스를 활용한 list 복사, list()
# # 복사본인 b, c, d의 값을 바꾸더라도 원본 a에는 아무런 변화가 없음
# # 원본이 바뀌면 복사본도 전부 바뀜
# a = [1, 2, 3]
# b = a.copy()
# c = a
# d = a[:]
# print(b)
# print(c)
# print(d)

# # copy하더라도 원본이 바뀌면 복사본도 따라서 바뀜.
# a1 = [1, 2, [8, 9]]
# b1 = a1.copy()
# c1 = a1
# d1 = a1[:]
# print(b1)
# print(c1)
# print(d1)
# a1[2][1] = 10
# print(a1)
# print(b1)
# print(c1)
# print(d1)
# # deepcopy() 원본이 바껴도 복사본은 안바뀌게 아예 새로운 주소를 만들어 버림.
# import copy
# e1 = copy.deepcopy(a1)
# print(a1)
# print(e1)
# a1[2][0] = 1000
# print(a1)
# print(e1)

# # for else -> for 문이 끝나면 else문 실행
# alist = ['1', '2', '3', '4']
# for _ in alist:
#     if _.startswith("1"):
#         print("1 이다.")
#     else:
#         print("1이 아니다.")
# else:
#     print("다 끝남")
