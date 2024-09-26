import os
import torch.multiprocessing as mp

class Python_Docs:
    def __init__(self):
        
        pass
    # Example for multiprocessing with Queue
    def multiprocess_queue(self):
        queue = mp.Queue()
        return queue

    # Example for reading a file
    def read_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return "File not found."

    # Example for writing to a file
    def write_file(self, file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)
        return "Write operation completed."

    # Example for basic math operation
    def add_numbers(self, a, b):
        return a + b

    # Example for string manipulation
    def reverse_string(self, string):
        return string[::-1]

    # Example for getting the size of a directory
    def get_directory_size(self, dir_path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(dir_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    # Example for checking if a number is prime
    def is_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Example for using map function
    def square_numbers(self, num_list):
        return list(map(lambda x: x**2, num_list))

    # Example for using filter function
    def filter_even_numbers(self, num_list):
        return list(filter(lambda x: x % 2 == 0, num_list))
    


if __name__ == "__main__":
    
    # Example usage:
    doc = Python_Docs()
    print(doc.add_numbers(5, 7))
    print(doc.reverse_string("hello"))
    print(doc.square_numbers([1, 2, 3, 4]))
    print(doc.is_prime(11))
    queue = doc.multiprocess_queue()