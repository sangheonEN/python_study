# # 람다식 매개변수 : 매개변수를 이용한 식
# # 람다식을 사용함으로서 함수의 정의 과정이 매우 짧아지고 간편해짐
add = lambda x, y: x+y
print(add(1, 2))

# map() : 다수의 원소에 대한 함수의 결과를 한 번에 얻을 수 있도록 도와줌.  리스트내의 각 원소에 접근해서 처리 하고 싶을 때
# 1과 6, 2와 7 ... 이런 규칙으로 더한 값을 출력하는 리스트를 만들고 싶다.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
my_function = lambda x, y : x*y
result = map(my_function, list1, list2)       # list1과 list2에 각 원소에 접근해서 my_function 함수를 사용해라.
print(list(result))                           # map 함수 원소를 list로 변환
