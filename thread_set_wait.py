import threading
import time


def before_f(evt_param):
    
    time.sleep(3)
    
    evt_param.set() # set되는 순간 after_f의 evt_param.wait()에서 넘어감.
    
    print("before work, done \n")
    

def after_f(evt_param):
    
        
    print("after work, waiting \n")
        
    evt_param.wait()
        
    print("after work, done \n")
        
        
        
def check_evt(evt_param):
    
    while True:
        time.sleep(0.5)
        if evt_param.is_set():
            print(f"evt_param.is_set() : {evt_param.is_set()}\n")
            break
        
        else:
            print(f"evt_param.is_set() : {evt_param.is_set()}\n")
            continue
        

if __name__ == "__main__":
    evt = threading.Event()
    
    t1 = threading.Thread(target=before_f, args=(evt,))
    t2 = threading.Thread(target=after_f, args=(evt,))
    t3 = threading.Thread(target=check_evt, args=(evt,))
    
    t2.start()
    t1.start()
    t3.start()
