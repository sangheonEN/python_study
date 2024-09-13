import torch.multiprocessing as mp

"""
프로세스는 자체 메모리 공간, 코드, 데이터 및 시스템 리소스를 갖춘 실행 중인 독립적인 프로그램입니다.
각 프로세스는 독립적으로 작동하며 메모리에 자체 주소 공간이 있습니다.

데이터 통신 

Queue를 사용하여 프로세스끼리 데이터를 주고 받을 수 있다.

Pipe를 활용해서 parents, child Pipe를 생성하고 데이터를 주고 받을 수 있다.

통신을 위해 IPC 메커니즘이 필요합니다.

"""

def worker(conn, queue):
    
    get_queue = queue.get(timeout=5)
    
    print(f"queue get data: {get_queue}")
    
    queue.put("Put queue!")
       
    # receive the data
    audio_data = conn.recv()

    print(f"child pipe received data: {audio_data}")
    # child pipe send함수가 호출되면, parent_pipe.recv()로 반환.
    conn.send("child response!")
    conn.close()


if __name__ == "__main__":


    # Pipe를 활용해서 parents, child Pipe를 생성하고 데이터를 주고 받을 수 있다.
    # Create pipe
    parent_pipe1, child_pipe1 = mp.Pipe()
    parent_pipe2, child_pipe2 = mp.Pipe()
    parent_pipe3, child_pipe3 = mp.Pipe()
    
    queue = mp.Queue()
    
    queue.put("Get Queue!")

    # start new processing
    # Process를 선언하는 code가 main에 있어야 함!

    process1 = mp.Process(target=worker, args=(child_pipe1, queue, ))
    process1.start()
    process2 = mp.Process(target=worker, args=(child_pipe2, queue, ))
    process2.start()
    process3 = mp.Process(target=worker, args=(child_pipe3, queue, ))
    process3.start()

    parent_pipe1.send("parent_pipe1")
    parent_pipe2.send("parent_pipe2")
    parent_pipe3.send("parent_pipe3")

    # recv함수가 호출되면, worker 함수로 넘어감.
    print(f"parent_pipe1 main process received : {parent_pipe1.recv()}")
    print(f"parent_pipe2 main process received : {parent_pipe2.recv()}")
    print(f"parent_pipe3 main process received : {parent_pipe3.recv()}")
    
    
    response1 = queue.get()
    print(f"response1 {response1}\n")
    response2 = queue.get()
    print(f"response2 {response2}\n")
    response3 = queue.get()
    print(f"response3 {response3}\n")
    
    print(f"queue : {queue}\n")
    
    
    # process ending point
    process1.join()
    process2.join()
    process3.join()
