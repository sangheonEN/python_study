import multiprocessing as mp

def process_function():
    while True:
        pass

if __name__ == "__main__":
        
    processes = []
    try:
        while True:
            p = mp.Process(target=process_function)
            p.start()
            processes.append(p)
            print(f"Process count: {len(processes)}")
    except Exception as e:
        print(f"Failed to create process: {e}")