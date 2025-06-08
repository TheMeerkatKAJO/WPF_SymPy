import sys
import numpy as np

def random_numbers(low, high, size):
    a = np.random.randint(low,high,size)
    return a

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Wrong script run: main.py <arg0> <arg1> <arg2>")
        
    size = int(sys.argv[1])
    low = int(sys.argv[2])
    high = int(sys.argv[3])

    res = random_numbers(low, high, size)
    print(res)