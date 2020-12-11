# 문자열 연산 및 개요
print("안녕 \"클레오\" 파트라~ 세상에서 \t제일 가\n는 포테\n이토 칩!")
a = "이d아"
b = "ddd"
print((a + b+"\t") * 5)

# 문자열 인덱싱 및 슬라이스 기법
a = "Hello World"
print((a[0]+a[3]))
print(a[-1])
print(a[2:3])
print(a[2:4])
print(a[2:5])
print(a[2:6])
print(a[2:7])
print(a[:-2])
print(a[0:-2])
print(a[1:-2])
print(a[:])
print(a[0:7:2]) # 0~7인덱스 까지 2씩 올라가면서 출력 a[0], a[2], a[4], a[6]

# 문자열 변환 replace(기존 문자열, 변환할 문자열) 다른 변수에 넣어 준 뒤에 사용할 수 있음
a = "HELLO WORLD DSAF"
c = "20"
# a.replace('HELLO','HIGH')
# print(a)
b = a.replace("HELLO", "HIGH")
print(b)
print(a.count('L'))
print(a.find('WORLD')) #해당 문자열이 맞지 않으면 -1 반환
print(a.upper()) # 대문자 변환
print(a.lower()) # 소문자 변환
print(a.strip("HELLO")) # 해당 문자열 빼고 나머지 문자열 출력
print(a.split(" ")) # 어떤 기준으로 문자열을 잘라서 각각의 문자열 배열로 만듬.
print(a.zfill(50)) # 변수로 넣는 정수 만큼 자리수를 만듬. 문자열이 자리수 보다 적으면 앞에 0을 채워 넣음.
print(c.zfill(5))
d = int(c)
print(d+2902)

# <<, >> 쉬프트 연산자, ** 거듭제곱 연산자, = 할당 연산자
a = 2
print(a << 4) # 1 -> 10000   왼쪽으로 4번
print(a >> 4) # 4번 오른쪽으로 옮기면 더 이상 이동할 수 없으니까 0
b = 10
print(a ** b) # 거듭 제곱 2의 10제곱
c = 20
print(c)
print(c == 19)



