# 특정한 조건을 만족할때만 소스코드를 반복적으로 수행
i = 0
sum = 0
while i <= 5:
    i = i+1
    if i % 2 == 1:
        continue
    sum = sum + i
print("합계 : ", sum)