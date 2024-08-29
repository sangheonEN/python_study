import torch.multiprocessing as mp

"""
프로세스는 자체 메모리 공간, 코드, 데이터 및 시스템 리소스를 갖춘 실행 중인 독립적인 프로그램입니다.
각 프로세스는 독립적으로 작동하며 메모리에 자체 주소 공간이 있습니다.

데이터 통신 

Queue를 사용하여 프로세스끼리 데이터를 주고 받을 수 있다.

Pipe를 활용해서 parents, child Pipe를 생성하고 데이터를 주고 받을 수 있다.

통신을 위해 IPC 메커니즘이 필요합니다.

"""

def worker(conn):
    
    # receive the data
    audio_data = conn.recv()

    print(f"child pipe received data: {audio_data}")

    conn.send("child response!")
    conn.close()


if __name__ == "__main__":


    # Pipe를 활용해서 parents, child Pipe를 생성하고 데이터를 주고 받을 수 있다.
    # Create pipe
    parent_pipe, child_pipe = mp.Pipe()

    # start new processing
    # Process를 선언하는 code가 main에 있어야 함!

    process1 = mp.Process(target=worker, args=(child_pipe, ))
    process1.start()

    parent_pipe.send("hello world")

    print(f"parent_pipe main process received : {parent_pipe.recv()}")

    # process ending point
    process1.join()
