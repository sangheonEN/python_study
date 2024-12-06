"""

스레드란 프로세스 내의 더 작은 실행 단위입니다. 

여러 스레드가 동일한 프로세스 내에 존재하여 동일한 메모리와 리소스를 공유

스레드는 동일한 프로그램 내에서 동시에 실행되어야 하고 백그라운드 작업을 수행하는 동안 사용자 인터페이스를 업데이트하는 것과 같이 리소스를 공유해야 하는 작업에 이상적

데이터 통신 방법 : 공유 변수를 통해 직접 통신할 수 있지만 문제를 피하기 위해 동기화가 필요합니다.

python thread docs 3.12.8 version 내용 검토 (https://docs.python.org/ko/3.12/library/threading.html#module-threading)

1. 


"""

import threading

def worker():

    print("ffffffffffff")


if __name__ == "__main__":

    thread_1 = threading.Thread(target=worker)
    thread_1.daemon = True
    thread_1.start()

    