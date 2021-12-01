# 7.1 번
# 출생년도에 대한 리스트 year_lists 만들어보자.
a = int(input())

year_lists = [number for number in range(a, a+6, 1)]
print(year_lists)

# 7.2 번 세 번째 생일은 몇년도?
print(year_lists[2])

# 7.3 번 years_list 중 가장 나이가 많은 년도?
print(year_lists[-1])

# 7.4 번

# 7.10 번 컴프리핸션을 이용해 range(10)에서 짝수 리스트 만들어 보자.
alist = [number for number in range(10) if number % 2 == 0]
print(alist[1:5])