# 문자열 뒤집기
str = "Hello World"
print(str[::-1])

# 문자열 길이
print(len(str))

# isalpha() : 특정한 문자열에 문자로만 이루어져있는지 bool값으로 출력 (띄어쓰기, 특수문자 있으면 false)
str = "Hello World"
str1 = "HelloWorld이상헌"
print("isalpha() :", str.isalpha(), str1.isalpha())

# isdigit() : 특정한 문자열이 숫자만 이루어져있는지 bool값으로 출력 (띄어쓰기, 특수문자 있으면 false)
str2 = "12345rr"
str3 = "12345"
print("isdigit() :", str2.isdigit(), str3.isdigit())

# isalnum() : 특정한 문자열이 문자 or 숫자로 이루어져있는지 bool값으로 출력 (띄어쓰기, 특수문자 있으면 false)
str4 = "12354sajnsa"
str5 = "1234"
str6 = "asdfsdg"
print(str4.isalnum(), str5.isalnum(), str6.isalnum())

# join(리스트자료형) : 여러개의 문자열을 구분자와 함께 합치는 함수. 리스트 자료형을 사용함
list1 = ["홍길동", "철구", "염보성", "이상헌"]
print(','.join(list1))                      # 구분자.join(list변수)

# sorted(문자열자료형) : 각 문자열 정렬
str7 = "hellowworld"
list2 = sorted(str7)           # 문자열 오름차순으로 정렬
print(list2)                   # 리스트 형태로 저장됨
print(''.join(list2))          # 공백 구분자로 문자열을 하나로 조인
list3 = sorted(str7, reverse= True)
print(list3)
print(''.join(list3))

# split(토큰) : 문자열을 토큰 기준으로 분리하는 함수
str8 = "i'm-a-good-boy"
list5 = str8.split("-")
print(list5)

# find() 문자열 내부에 문자열 찾기 (해당 문자열이 없을 경우 -1 출력, 해당 문자열이 있는 경우 제일 앞에 문자의 인덱스 출력, 중복된 문자가 있으면 제일 앞의 문자기준으로 출력)
str10 = "i like like you"
print(str10.find("like"))
print(str10.find("tid"))
print(str10.find("like", 5)) # 5 다음 인덱스부터 찾겠다!

# upper(), lower()
str11 = "sdafjnmiADUBQWDWJ"
print(str11.upper())
print(str11.lower())

# strip() 좌우로 특정한 문자열을 제거하는 함수
str12 = "  ff asdsa ff  "
str13 = "ff asdsa ff"
print(str12.strip())
print(str12.lstrip())
print(str12.rstrip())
print(str13.strip("f"))
print(str13.lstrip("f"))
print(str13.rstrip("f"))

# eval() 문자열 수식을 계산해주는 함수
exp = "(13+203)*131-233"
print(eval(exp))












