# 리스트 컴프리핸션 : for/in 문의 순회 기능을 가진 리스트 컴프리헨션을 통해 리스트를 생성
# 표현식 for 항목 in 순회 가능한 객채(range()) if 조건.

# for/in 사용 리스트 생성 방식
alist = []
for num in range(1, 6):
    if num % 2 != 0:
        alist.append(num)
print(alist)

# 리스트 컴프리핸션 사용 리스트 생성 방식
blist = [number for number in range(1,6) if number % 2 != 0]
print(blist)

# 2차원 배열 생성
# 이중 포문 사용
print("rows = ", [1, 2, 3, 4])
print("cols = ", [1, 2, 3])
rows = range(1,4)
cols = range(1,3)

print("""for row in rows:
    for col in cols:
        print(row, col)""")
for row in rows:
    for col in cols:
        print(row, col)
print("\n")
# 리스트 컴프리핸션 사용 -> 출력이 튜플로 됨
print("cells = [(row,col) for row in rows for col in cols]")
cells = [(row,col) for row in rows for col in cols]
for cell in cells:
    print(cell)
print("\n튜플 언패킹")
# 튜플 언패킹
for row, col in cells:
    print(row, col)