import threading

# 플래그를 사용하여 스레드를 제어
stop_threads = False

def input_thread():
    global stop_threads
    while not stop_threads:
        user_input = input()
        if user_input.lower() == 'x':  # 'x' 입력 시 종료 확인
            stop_threads = True
        else:
            print(f"{user_input}!")

def main():
    global stop_threads
    # 입력 받는 스레드 시작
    thread = threading.Thread(target=input_thread)
    thread.start()

    # 스레드가 종료될 때까지 대기
    while not stop_threads:
        pass

    # 프로그램 종료 여부 묻기
    confirm = input("프로그램을 종료하시겠습니까? (y/n): ").strip().lower()
    if confirm == 'y':
        print("프로그램을 종료합니다.")
        stop_threads = True  # 명시적으로 종료
        thread.join()
    else:
        print("프로그램을 재시작합니다.")
        stop_threads = False
        main()  # 재귀적으로 main 재실행

if __name__ == "__main__":
    main()
