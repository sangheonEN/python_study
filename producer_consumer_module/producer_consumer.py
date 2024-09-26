import torch.multiprocessing as mp
import time


def producer(queue, event, buffer_size):
    
    for i in range(1, 11):
        
        while queue.qsize() >= buffer_size:
            print("Buffer is full. waiting...\n")
            time.sleep(0.5)
        
        time.sleep(1)
        item = f'Item {i}'
        print(f"Produced : {item}\n")
        queue.put(item)
        
    event.set()
    

def consumer(queue, event):
    
    while not event.is_set() or not queue.empty():
              
        if not queue.empty():
            item = queue.get()
            print(f"Consumed : {item}\n")
            time.sleep(5.0)

        else:
            time.sleep(1.0)

    
if __name__ == "__main__":
    buffer_size = 5
    event_queue = mp.Queue() # data queue
    event_enable_flag = mp.Event() # 이벤트 발생 trigger
        
    producer_process = mp.Process(target=producer, args=(event_queue, event_enable_flag, buffer_size))
    consumer_process = mp.Process(target=consumer, args=(event_queue, event_enable_flag))
    
    producer_process.start()
    consumer_process.start()
    
    producer_process.join()
    consumer_process.join()
    
    print("All Process Finished")