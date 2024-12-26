# 같은 이름의 함수가 다른 동작을 하게 만들기.

class Student_1:
    
    def __init__(self, money):
        
        self.money = money
        
    def payback(self):
        
        return self.money * 20

class Student_2:
    
    def __init__(self, money):
        
        self.money = money
        
    def payback(self):
        
        return self.money * 2



person1 = Student_1(10)
person2 = Student_2(10)

print(f"person1 payback: {person1.payback()}")
print(f"person2 payback: {person2.payback()}")