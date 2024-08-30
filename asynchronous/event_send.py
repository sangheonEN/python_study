import socket
import time

def send_event_parameter():
    host = '127.0.0.1'  # 서버 IP 주소
    port = 12345        # 서버 포트

    while True:
        try:
            # TCP 소켓 생성
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))  # 서버에 연결
                message = '1'            # 이벤트 파라미터
                s.sendall(message.encode())  # 메시지 전송
                print(f"Sent event parameter: {message}")

            time.sleep(2)  # 3초 대기

        except ConnectionRefusedError:
            print("Server not available, retrying in 10 seconds...")
            time.sleep(3)  # 서버가 없을 때 3초 후 재시도

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(3)  # 다른 오류 발생 시 3초 후 재시도

if __name__ == "__main__":
    send_event_parameter()
