# 튜플(Tuple) : 리스트(List)와 비슷한 자료형 But 한번 설정(입력)된 값은 변경이 불가하다.
# tuple = (1, 2, 3)
# for i in tuple:
#     print(i)
#
# list1 = [1, 2, 3]
# list2 = [2, 3, 4]
# tuple2 = (list1, list2)
# for i in tuple2:
#     print(i)

# 튜플의 원소 자체는 변경 못하지만, 튜플 내부에 리스트가 있을때 리스트의 인덱스에 접근해서 리스트 원소를 변경할 수는 있다.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# tuple = (list1, list2)
# # tuple[0] = (7, 8, 9)
# tuple[0][1] = 8
# for i in tuple:
#     print(i)

# 튜블 연산 표현법
# tuple = (1, 2, 3, 4, 5, 6, 7, 8)
# print(tuple[0:5] * 3)


