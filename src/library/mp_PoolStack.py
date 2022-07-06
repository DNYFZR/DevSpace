# Python Multiprocessing Pool Class 
from multiprocessing import Pool, cpu_count
from numpy import array, float16
from functools import cache

class pool_stack:
    def __init__(self, data, func, cpu_workers = cpu_count(), output_dtype = float16):
        self.workers = cpu_workers 
        self.data = data
        self.func = func
        self.output = array(list([]), dtype=output_dtype)
    
    def pool_handler(self):
        with Pool(self.workers) as pool:
            self.output = pool.map(self.func, self.data)
        return self.output

@cache
def f(x): 
    return x**2 + x**3 / 3 + x**4 / 4

if __name__ == '__main__':
    from time import time
    data = [i for i in range(25000001)]
    print(f'Test data size : {max(data)}\n')
    
    start = time() 
    stack = pool_stack(data=data, func=f).pool_handler()
    stack_time = time()
    
    with Pool(cpu_count()) as pool:
            new_data = pool.map(f, data)
    pool_lap = time()

    base = [f(i) for i in data]
    end = time()

    print(f'base:{end - pool_lap}\nstack:{stack_time - start}\npool loop: {pool_lap - stack_time}')