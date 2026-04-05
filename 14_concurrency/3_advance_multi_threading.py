### Multithreading with Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time 

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"
    


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]        

#             Normal Execution
# start_time = time.time()
# for num in map(print_number, numbers):
#     print(num) 
# end_time = time.time()
# print(f"Execution Time: {end_time - start_time:.2f} seconds")     # Output: 15.1 seconds


#             Thread Pool Executor

start_time = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)

for result in results:
    print(result)
end_time = time.time()
print(f"Execution Time: {end_time - start_time:.2f} seconds")    # Output: 5.01 seconds