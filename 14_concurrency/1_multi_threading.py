# Multithreading

## When to use Multi Threading
###I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading 
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f'Number: {i}')
        
def print_letter():
    for letter in "abcde":
        time.sleep(2) 
        print(f"Letter: {letter}")

#                         Normal Execution
# start_time = time.time()
# print_numbers()
# print_letter()
# end_time = time.time()
# print(f"Execution Time: {end_time - start_time:.2f} seconds")          # Output: 20.1 second


#                       Multi Threading
# create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

start_time = time.time()
# start the thread
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()

end_time = time.time() 
print(f"Execution Time: {end_time - start_time:.2f} seconds")      # Output: 10.01 seconds

