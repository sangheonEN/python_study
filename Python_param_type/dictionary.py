# # 생성방법
# # case1
# my_dict = {}               # 딕셔너리 초기화 및 선언
# my_dict["a"] = "aaa"
# my_dict["b"] = "bbb"
# my_dict["c"] = "ccc"
# print(my_dict)
# # case2
# dict1 = {"aa" : "aaa", "bb" : "bbb"}
# print(dict1)

# 사전(dictionary) : key와 value의 한 쌍을 원소로 가지는 자료형
dict = {}
dict["이름"] = "name"
dict["기적"] = "miracle"
dict["노력"] = "effort"

# # 원소 내용 변경 키값을 이용해 변경
# dict["이름"] = "SangHeon"
#
# # key 값만 출력
# keys = dict.keys()
# print("키 :", keys)
# keyslist = list(keys)
# print("키 리스트 :", keyslist)

# # value 값만 출력
# values = dict.values()
# print("values :", values)
# valueslist = list(values)
# print("values 리스트 :", valueslist)

# 모든 값 출력 items()
items1 = dict.items()
print("items : {}".format(items1))

# 길이 얻기 len()
print(len(items1))

# 결합하기 {**a, **b} a, b의 원소는 변하지 않음.
print("결합하기")
a = {1:2, 3:4, 5:6}
b = {7:8, 9:10, 11:12}
c = {**a, **b}
print(f"a = {a}, b = {b}")
print("c = {**a, **b} =", c)

# a.update(b) a에 b를 집어넣어서 a의 값을 바꿔줌.
a.update(b)
print("a.update(b) =", a)

#

# # if 문에 사용
# if '노력' in dict:
#     print("[노력] 키가 존재합니다.")
#
# # 키 값으로 원소 삭제 del dict["키값"]
# del dict["기적"]
# print(dict)
# for i, k in enumerate(dict):
#     print("인덱스", i, "번째 한글 단어는", k, "이고 영어 단어는", dict[k], " 입니다.")
#
# # 모든 원소 삭제
# dict.clear()
# print(dict)
# print("사전의 글씨 길이 :", len(dict))

# # 정렬하기
# score = {}
# score["이상헌"] = 100
# score["박순홍"] = 95
# score["김규태"] = 90
# score["김하영"] = 100
# # key 값으로 정렬하기
# print(sorted(score))                         # 오름차순
# print(sorted(score, reverse = True))         # 내림차순
# # value으로 정렬하기
# print(sorted(score.values()))                # 오름차순
# print(sorted(score.values(), reverse=True))  # 내림차순

# 키로 항목 가져온 뒤 삭제하기 pop()


# 키 멤버십 테스트 in

# 딕셔너리 비교는 ==과 != 만 사용가능

# copy(), deepcopy()

# for와 in으로 순회


# # set : 값은 버리고 키만 남은 딕셔너리와 같다.
# # 리스트와의 차이 set은 순서가 없다. list는 순서가 있다.
# a = {1, 2, 3, 4, 5} # set
# b = [1, 2, 3, 4, 5] # list
# print(a)
# print(b)

# # 멤버십 테스트 : in
# drinks = {
#     'milk' : {'vodka', 'vermouth'},
#     'black label' : {'vodka', 'kahlua'},
#     'white wine' : {'crae', 'dsfadf', 'cream'},
#     'manhattan' : {'sad', 'happy', 'vermouth'}
# }
# print("음료 성분 : {}".format(drinks))
# # 보드카가 들어간 음료를 마시고 싶다. (딕셔너리 안의 값 영역에서 set으로 선언된 vodka를 찾아서 그에 맞는 키 값을 출력해라.)
# print("보드카가 들어간 음료를 마시고 싶다. (딕셔너리 안의 값 영역에서 set으로 선언된 vodka를 찾아서 그에 맞는 키 값을 출력해라.)")
# for name, contents in drinks.items():
#     if 'vodka' in contents:
#         print(name)
#
# # 보드카가 들어있지만, vermouth와 cream이 들어간 음료는 먹기 싫다.
# print("보드카가 들어있지만, vermouth와 cream이 들어간 음료는 먹기 싫다.")
# for name, contents in drinks.items():
#     if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
#         print(name)

# # 콤비네이션 연산자
# drinks = {
#     'milk' : {'vodka', 'vermouth'},
#     'black label' : {'vodka', 'kahlua'},
#     'white wine' : {'crae', 'dsfadf', 'cream'},
#     'manhattan' : {'sad', 'happy', 'vermouth'},
#     'juice' : {'orange juice', 'cola', 'cock', 'sida'}
# }

# # 오렌지 주스나 베르무트가 들어 있는 음료를 마시고 싶다. & 기호 사용
# print("오렌지 주스나 베르무트가 들어 있는 음료를 마시고 싶다.")
# for name, contents in drinks.items():
#     if contents & {'vermouth', 'orange juice'}:
#         print(name)

# # & or intersection() : 교집합을 구하자.
# a = {1, 2}
# b = {2, 4}
# print(a & b)
# print(a.intersection(b))

# | or union() 합집합 구하자.

# - or difference() 차집합 구하자.

