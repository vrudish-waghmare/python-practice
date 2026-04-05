'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing
import math 
import sys 
import time 

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [200, 300, 400, 500, 600]

    start_time = time.time()
    ##create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)
    
    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")          # Output: 0.73 seconds
    
