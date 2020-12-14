# 리스트 : 변수가 많을 때는 리스트를 쓰자! 비슷한 속성(같은 자료형을 가진 데이터의 나열이다.)
# 인덱스 : 0    1    2    3    ~
# 값    : 2.3 3.3  4.3  5.3
# c언어의 배열과는 다르게 list 안에 많은 잠재함수들이 있어 연속된 값을 표현하고 처리하기 아주 용이하다.
# a = [3.5, 12.3, 23.4, 1.3]
# print(a)
# # 개별 원소 접근
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# # 원소 값 변경
# a[1] = 2.1
# print(a[1])
# # 반복문 사용
# sum = 0                # 초기 값 선언
# for i in a: # i 는 a 안에 들어있는 원소들을 처음부터 차례대로 나타냄
#     sum = sum + i
# print("평균 점수 :", sum/len(a))

# 리스트 안의 리스트 a[0] = 학생들의 영어 점수, a[1] 학생들의 수학 점수
# sum = 0
# a = [[90, 80, 30, 40, 50], [100, 30, 60, 70, 10]]
# english = a[0]
# for i in english:
#     sum = sum + i
# print("영어 평균 점수 : ", sum / len(english))
# sum = 0
# math = a[1]
# for i in math:
#     sum = sum + i
# print("수학 평균 점수 : ", sum / len(math))

# 리스트 함수
# a = [10, 20, 30, 40, 50, 10, 10]
# b = [20, 30, 50]
# print(a)
# print(a.count(10))   # count(데이터) 리스트 내의 특정 원소가 몇개 포함되어 있는지 정수형으로 반환
# print(a.index(50))   # index(데이터) 리스트 내의 특정 원소가 몇 번째 자리에 있는지 정수형으로 반환
# a.append(25)         # append(데이터) 리스트 순서 마지막에 데이터를 넣어줌
# print(a)
# a.sort()             # sort() 자동으로 오름차순으로 정렬해줌
# print(a)
# a.reverse()          # reverse() 뒤에서부터 출력해줌
# print(a)

# 리스트 더하기
# a.extend(b)          # 리스트.extend(다른 리스트) 리스트 마지막 순서부터 다른 리스트의 원소가 들어감
# print(a)
# a.insert(3, 1000)    # insert(몇 번째 인덱스, 넣을 데이터) 몇 번째 인덱스에 특정한 데이터를 넣음
# print(a)
# a.remove(1000)       # remove 리스트내의 특정한 원소를 찾아서 없앰
# print(a)
# print(a.pop(0))      # pop 리스트내의 특정한 원소를 찾아서 출력함

# 숫자형 list 변수를 문자열 list변수로 넣기
alist = [1, 2, 3, 4, 5]
blist = []
for a in alist:
    blist.append(str(a))
print(blist)

# sep = ""
print("1","2","3")
print("1","2","3", sep= "|")



