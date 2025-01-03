import torch.multiprocessing as mp
import time
"""
프로세스는 자체 메모리 공간, 코드, 데이터 및 시스템 리소스를 갖춘 실행 중인 독립적인 프로그램입니다.
각 프로세스는 독립적으로 작동하며 메모리에 자체 주소 공간이 있습니다.

데이터 통신 

Queue를 사용하여 프로세스끼리 데이터를 주고 받을 수 있다.

Pipe를 활용해서 parents, child Pipe를 생성하고 데이터를 주고 받을 수 있다.

통신을 위해 IPC 메커니즘이 필요합니다.

"""

def worker(conn, start_time):
      
    # receive the data
    
    if conn.poll(0.1): # poll은 데이터가 전송받은 데이터가 있는지 확인 flag. 있으면, 대기시간(0.1) 무시하고 곧 바로 실행 
        audio_data = conn.recv()

    end_time = time.time()
    print(f"process time : {round(end_time-start_time, 2)}")
    print(f"child pipe received data: {audio_data}")
    # child pipe send함수가 호출되면, parent_pipe.recv()로 반환.
    conn.send("child response!")
    conn.close()


if __name__ == "__main__":
    
    start_time = time.time()
    
    # Pipe를 활용해서 parents, child Pipe를 생성하고 데이터를 주고 받을 수 있다.
    # Create pipe
    parent_pipe, child_pipe = mp.Pipe()

    # start new processing
    # Process를 선언하는 code가 main에 있어야 함!

    process1 = mp.Process(target=worker, args=(child_pipe, start_time))
    process1.start()

    time.sleep(3)
    parent_pipe.send("hello world")

    # recv함수가 호출되면, worker 함수로 넘어감.
    print(f"parent_pipe main process received : {parent_pipe.recv()}")

    # process ending point
    process1.join()
