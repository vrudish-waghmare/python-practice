# Multi processing

### CPU-Bound Tasks-Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
## Parallel execution- Multiple cores of the CPU

import multiprocessing
import time 

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i * i * i}")  

#              Normal Execution
# start_time = time.time()
# square_numbers()
# cube_numbers()
# end_time = time.time()
# print(f"Execution Time: {end_time - start_time:.2f} seconds")      # Output: 12.53 seconds


#            Multi Processing
if __name__=="__main__":

    # Create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    start_time = time.time()
    # start the process
    p1.start()
    p2.start()

    # Wait for the process to complete
    p1.join()
    p2.join()

    end_time = time.time()
    print(f"Execution Time: {end_time - start_time:.2f} seconds")          # Output: 7.81 seconds
