# 미리 작성된 함수 코드를 모아 놓은 파이썬 파일! 라이브러리를 직접 만들어서 끌고와서 쓸수있고 다른 사람에게 제공할수도있다.
# 다양한 기능별로 만들어서 모듈화할수있다.
# import math
# print(math.pow(2, 4))   # 제곱 함수
# print(math.sqrt(60))    # 제곱근 함수
# print(math.gcd(10, 20)) # 최대 공약수

# 라이브러리 연동하기 위해 선언하기 import + 파일명
# import lib
# print(lib.add(1, 2))
# print(lib.substract(2, 3))

# 라이브러리의 하나의 함수를 쓰고 싶을때 선언함.
# from lib import add
# print(add(1, 2))

# 라이브러리 이름 간략하게 줄이기  as 별칭
# import lib as t
# print(t.substract(1, 2))