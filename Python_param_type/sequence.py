# sequence 자료형 : 문자열, 리스트, 튜블 자료형에 index를 가지는 자료형
string = "Hello World"
tuple = ('H','e','l','l','o',' ','W','o','r','l','d')
list = ['H','e','l','l','o',' ','W','o','r','l','d']

print(string[0:5])
print(tuple[0:5])
print(list[0:5])

for i in string:
    if i == 'H':
        print("난 H이다.")
for i in tuple:
    if i == 'H':
        print("난 H이다.")
for i in list:
    if i == 'H':
        print("난 H이다.")

# len() 함수를 이용한 변수의 길이 측정
string2 = "sadfsdaf"
string = "sadgg"
print(len(string+string2))

# in
list1 = [1, 2, 3, 4]
print(4 in list1)
print(6 in list1)



