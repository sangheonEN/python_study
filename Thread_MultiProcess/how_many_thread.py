import threading


def thread_function():
    while True:
        pass


if __name__ == "__main__":

    threads = []
    try:
        while True:
            t = threading.Thread(target=thread_function)
            t.start()
            threads.append(t)
            print(f"Thread count: {len(threads)}")
    except Exception as e:
        print(f"Failed to create thread: {e}")
