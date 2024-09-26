# 데코레이터의 존재 이유 : 동일한 함수를 반복적으로 활용하기 위함


class Deco:
    def __init__(self) -> None:
        pass
    
    
    
    def basic_decorator():
        pass
    
    @staticmethod
    def static_function(param1, param2):
        """
        - 특징 -
        1. @staticmethod 데코레이터는 self를 매개변수로 지정하지 않음.
        2. self 변수나 함수를 명시적으로 인수로 전달받아 인스턴스 데이터와 함께 작동 가능.
        
        - 활용처 및 활용법 -
        1. 활용처 : 클래스내에 다른 인스턴스 메서드나 속성을 수정하거나 액세스할 필요가 없는 작업을 수행 ex) 멀티프로세스에 들어가는 함수로 사용
        2. 활용법 : 클래스에서 바로 메서드 호출
        
        """
        
        return param1 + param2
        
        
        
        


if __name__ == "__main__":
    
    # staticmethod 활용법
    print(Deco.static_function(10, 20))
    
    
    

    