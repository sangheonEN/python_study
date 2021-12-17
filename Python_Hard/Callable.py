import torch
"""
- python에서 magic method는 클래스 인스턴스가 함수처럼 작동하도록 만들 수 있다.
- 한 함수를 다른 함수로 전달하는 작업을 수행
- call(self, [args ...])
- 현재까지 내가 안 내용은 pytorch의 Hook Class를 만들어서 register_forward, backword 부분에서 callable 문법이 사용됨
"""

# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __call__(self, x, y):
#         self.x, self.y = x, y
#
#     def __str__(self):
#         return '(%s, %s)' % (self.x, self.y)
#
#
# def index(a, b, c):
#     a = 3
#     b = 3
#     c = 3
#     return f"index page{a+b+c}"
#
# class Indexview(object):
#     def __call__(self,):
#         return "index view page"
#
# def visit_website(view):
#     print(view())

class A():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(self.x, self.y)

    def __call__(self, *input, **kwargs):
        return f"call function is adding: {self.x + self.y}"


def b(a, b):
    print(a, b)

if __name__ == "__main__":
    # c1 = Coordinate(1, 2)
    # print(callable(c1))
    #
    # c1(2, 3)
    # print(c1)

    # visit_website(index)
    # visit_website(Indexview())

    a = A(10, 2)
    a(b)

