# # 튜플 생성하기
# empty_tuple = (1, 2, 3)
# empty_tuple2 = 1, 2, 3,      # 끝에 ,를 붙여줌
# empty_tuple3 = (1, 2, 3,)    # 괄호 안 끝에 , 붙이기
# print(empty_tuple)
# print(empty_tuple2)
# print(empty_tuple3)
# empty_tuple4 = ("asdsaf")    # 괄호 안에 문자열 넣으면 문자열로 출력! 주의!
# print(empty_tuple4)

# # 튜플 활용 튜플 언패킹 (한번에 여러 변수를 할당할 수 있음)
# aabbcc = ('aa', 'bb', 'cc')
# a, b, c = aabbcc
# print(a)
# print(b)
# print(c)

# swap 가능

# tuple() 형변환

# + 결합 가능

# * 복제 가능

# 비교 가능

# # 순회 for in
# tuple1 = ('a', 'b', 'c')
# for _ in tuple1:
#     print(_)
#
# # tuple를 더한다고 본래의 tuple이 변하지 않는다. 하지만 할당 연산자 = 을 사용하면 변경된다.
# atuple = (10, 20, 30)
# btuple = (40, 50, 60)
# print(atuple + btuple)
# print(atuple)
# print(btuple)
# atuple = btuple
# print(atuple)

# # 튜플(Tuple) : 리스트(List)와 비슷한 자료형 But 한번 설정(입력)된 값은 변경이 불가하다.
# tuple = (1, 2, 3)
# for i in tuple:
#     print(i)
#
# list1 = [1, 2, 3]
# list2 = [2, 3, 4]
# tuple2 = (list1, list2)
# for i in tuple2:
#     print(i)
#
# # 튜플의 원소 자체는 변경 못하지만, 튜플 내부에 리스트가 있을때 리스트의 인덱스에 접근해서 리스트 원소를 변경할 수는 있다.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# tuple = (list1, list2)
# # tuple[0] = (7, 8, 9)
# tuple[0][1] = 8
# for i in tuple:
#     print(i)
#
# # 튜블 연산 표현법
# tuple = (1, 2, 3, 4, 5, 6, 7, 8)
# print(tuple[0:5] * 3)
