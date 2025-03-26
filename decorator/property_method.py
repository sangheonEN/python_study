# property 데코레이터를 사용한 방법
class Customer_property:

    def __init__(self, name, age):
            self._name = name
            self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

# 일반 메서드를 사용한 방법
class Customer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

if __name__ == "__main__":
    
    # 일반 메서드를 사용한 방법
    c = Customer('John', 30)
    print("get_name: ", c.get_name()) # getter 호출
    print("set_name: ", c.set_name('Jane')) # setter 호출
    
    # property 데코레이터를 사용한 방법
    c = Customer_property('John', 30)
    print("name: ", c.name) # getter 호출
    c.name = 'Jane' # setter 호출
    print("name: ", c.name) # getter 호출