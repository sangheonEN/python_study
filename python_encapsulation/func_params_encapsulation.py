class Person:
    def __init__(self, age):
        self.__age = age
        
    # 캡슐화된 변수를 읽기 (get)
    def get_age(self):
        return self.__age
    # 캡슐화된 변수를 변경 (set)
    def set_age(self, age):
        self.__age = age

    # 캡슐화된 함수 str형식으로 변경해서 age 출력
    def __str__(self):
        return f"{self.__age}"
    

a = Person(18)

# 외부에서 접근해서 __age의 값을 변경해보자!
a.__age = 10

print(f"age get: {a.get_age()}")
a.set_age(20)
print(f"age get: {a.get_age()}")
print(f"type trans str: {type(a.__str__())}")