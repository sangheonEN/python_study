lan1 = 10
lan2 = 9
lan3 = 11
print("lan = {} {} {}".format(lan1, lan2, lan3))

# 선언을 먼저 해도 매개변수 따라서 출력 됨.
def aaa(a, b,d,c):
    print("a = {}".format(a))
    print("b = {}".format(b))
aaa(b = "bbb", a = "aaa",c = "cccc",d="dddd")

# "{1} {0}".foramt(a, b)  a = 0 번째 b = 1 번째
print("{} = {}".format("a","b"))
print("{1} = {0}".format("a","b"))

# 보간문자 f-문자열 f'{변수명} {변수명}'
thing = "era"
place = "home"
print(f'The {thing} is in the {place}')
print(f"the {thing.capitalize()} is in the {place.rjust(20)}")
int1 = 10
int2 = 20
print(f'int1 : {int1}, int2 : {int2}')

# 보간 문자(f)
a = "aaa"
b = "bbb"
print(f"{b} = {a}")













import cv2

image = cv2.imread("format().PNG", cv2.IMREAD_COLOR)
cv2.imshow("format()", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

