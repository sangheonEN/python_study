import torch.multiprocessing as mp
import time

def is_event(event_flag):
    
    while (True):
        for i in range(3):
            time.sleep(2)
            print(f"count : {i+1}\n")
            print(f"what is the event state? {event_flag.is_set()}\n")
            
        print("count finish\n")  
        event_flag.set()
        break
    
    print(f"what is the event state? {event_flag.is_set()}\n")


if __name__ == "__main__":

    mp_event1 = mp.Event()
    
    mp_event1.clear()
        
    print(f"mp_event1.clear() -> mp_event1: {mp_event1.is_set()}")
    
    is_event(mp_event1)