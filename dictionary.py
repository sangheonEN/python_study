# 생성방법
# case1
my_dict = {}               # 딕셔너리 초기화 및 선언
my_dict["a"] = "aaa"
my_dict["b"] = "bbb"
my_dict["c"] = "ccc"
print(my_dict)
# case2
dict1 = {"aa" : "aaa", "bb" : "bbb"}
print(dict1)

# 사전(dictionary) : key와 value의 한 쌍을 원소로 가지는 자료형
dict = {}
dict["이름"] = "name"
dict["기적"] = "miracle"
dict["노력"] = "effort"

# 원소 내용 변경 키값을 이용해 변경
dict["이름"] = "SangHeon"

# key 값만 출력
keys = dict.keys()
print("키 :", keys)
keyslist = list(keys)
print("키 리스트 :", keyslist)

# value 값만 출력
values = dict.values()
print("values :", values)
valueslist = list(values)
print("values 리스트 :", valueslist)

# if 문에 사용
if '노력' in dict:
    print("[노력] 키가 존재합니다.")

# 원소 삭제
del dict["기적"]
print(dict)
for i, k in enumerate(dict):
    print("인덱스", i, "번째 한글 단어는", k, "이고 영어 단어는", dict[k], " 입니다.")

# 모든 원소 삭제
dict.clear()
print(dict)
print("사전의 글씨 길이 :", len(dict))

# 정렬하기
score = {}
score["이상헌"] = 100
score["박순홍"] = 95
score["김규태"] = 90
score["김하영"] = 100
# key 값으로 정렬하기
print(sorted(score))                         # 오름차순
print(sorted(score, reverse = True))         # 내림차순
# value으로 정렬하기
print(sorted(score.values()))                # 오름차순
print(sorted(score.values(), reverse=True))  # 내림차순




