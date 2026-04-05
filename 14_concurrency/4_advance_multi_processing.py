#  Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time 

def square_number(number):
    time.sleep(2)
    return f"Square: {number * number}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#             Normal Execution
# start_time = time.time()
# for square in map(square_number, numbers):
#     print(square) 
# end_time = time.time()
# print(f"Execution Time: {end_time - start_time:.2f} seconds")     # Output: 30.1 seconds


if __name__=="__main__":

    start_time = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)
    
    for result in results:
        print(result)
    
    end_time = time.time()
    print(f"Execution Time: {end_time - start_time:.2f} seconds")    # Output: 10.43 seconds