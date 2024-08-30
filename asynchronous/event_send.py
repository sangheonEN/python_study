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
            
            time.sleep(10)  # 10초 대기

        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    send_event_parameter()
