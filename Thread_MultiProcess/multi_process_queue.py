import torch.multiprocessing as mp
import torch

def worker(queue):
    try:
        print("Child process started")  # 프로세스 시작 시 출력
        audio_data = queue.get(timeout=5)
        print(f"Child process received data: {audio_data}")
        if not isinstance(audio_data, str):
            raise ValueError("Received data is not of type str")
        queue.put("Child response!")
        print("Child process sent response")  # 응답 전송 시 출력
    except Exception as e:
        print(f"Error in child process: {str(e)}")


if __name__ == "__main__":

    NGPU = torch.cuda.device_count()

    # Queue 객체를 생성합니다.
    queue = mp.Queue()
    
    # 부모 프로세스에서 데이터를 큐에 넣습니다.
    queue.put("Hello world")

    # 새로운 프로세스를 시작합니다.
    process1 = mp.Process(target=worker, args=(queue,))
    process1.start()

    # 프로세스가 종료될 때까지 기다립니다.
    process1.join()

    try:
        # 큐에서 자식 프로세스의 응답을 받습니다.
        response = queue.get(timeout=5)  # 타임아웃을 설정하여 블로킹 방지
        print(f"Parent process received: {response}")
    except Exception as e:
        print(f"Error in parent process: {str(e)}")
