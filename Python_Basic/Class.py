# 클래스 : 반복되는 불필요한 소스코드를 줄이고 현실세계의 사물의 특성을 컴퓨터 프로그래밍 상에서 쉽게 표현할 수 있다.
# 인스턴스 : 클래스로 정의된 객체를 프로그램상에서 이용할 수 있게 만든 변수
# 클래스의 변수, 함수(메소드)

# class Car:
#     # 클래스의 생성자 항상 함수형태로 존재 기본 형태 : def __init__(self):
#     def __init__(self, name, color):
#         self.name = name         # 클래스의 멤버
#         self.color = color       # 클래스의 멤버
#     # 소멸자                                         --> 너무 많이 메모리 상에 함수 변수들이 있으니까 사용한 후에 그냥 없애 버릴려고 소멸자 씀
#     def __del__(self):
#         print("인스턴스를 소멸시키겠습니다.")
#     # 클래스의 메소드
#     def show_info(self):
#         print("이름 : ", self.name)
#         print("색깔 : ", self.color)
#     # setter 메소드
#     def set_name(self, name):
#         self.name = name
#
# car1 = Car("소나타", "빨강색")
# car1.set_name("기모띠")
# print(car1.name, "을 구매 했습니다.")
# car1.show_info()
# del car1
# car2 = Car("마세라티", "검은색")
# car2.show_info()
# del car2


# 상속 : 다른 클래스의 멤버와 메소드를 물려받아서 사용한다.
# 부모와 자식관계가 존재하지 자식 클래스는 부모 클래스의 멤버와 메소드를 사용할 수 있다.
# 소스 코드를 줄이고 계층적으로 코드를 구성할 수 있다.
# 부모는 대분류 자식은 중, 소분류 ex) 게임 전체에서 Unit에 대한 이름과 전투력의 정보를 가지고 있는 부모 클래스를 사용해서 몬스터, 사용자로 나누어 이름과 전투력을 보고 싶다면 부모클래스 : Unit, 자식클래스 : 몬스터, 사용자로 나누어 정의해보자.
class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(self.name, "가 공격했고 전투력은 ", self.power, "입니다.")
unit = Unit("이상헌", 100)
unit.attack()

class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type
    def show_info(self):
        print("몬스터의 이름은", self.name, "이고 타입은", self.type, "이다.")

monster = Monster("개구리", 10, "1급")
monster.attack()
monster.show_info()

















