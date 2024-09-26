# 특정한 구문에 오류가 발생시 그것을 정상적으로 체크할 수 있다.
# try: except: 구문
try:
    print(3/0)
except:
    print("0으로는 나눌 수 없습니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:                               # 예외가 발생하든 말든 무조건 실행!
    print("예외처리를 마쳤습니다.")

try:
    print(3/1)
except:
    print("0으로는 나눌 수 없습니다.")
else:                                  # 예외가 발생하지 않았을때 실행!
    print("예외가 발생하지 않았습니다.")

# Exception 객체 사용 : 오류 내용을 출력하기 위해 사용
try:
    print(3/0)
except Exception as e:
    print(e)

