# General Multiprocessing Model v1
import multiprocessing as mp, numpy as np

class parallelogram:
    '''
        This class uses the multiprocessing library to parallelise the mapping of a user defined function to a an input array.
        Users can set the cpu_limit, otherwise it will automatically use all processors. 
        The class returns a numpy array.
    '''

    def __init__(self, input_data, process_function, cpu_limit = mp.cpu_count()):
        self.max_pool = cpu_limit

        self.data = input_data
        self.func = process_function
        self.output = np.array(list([]), dtype=np.float32)
    
    def __pool_handler(self):
        with mp.Pool(self.max_pool) as pool:
             self.output = pool.map(self.func, self.data)

    def run_stack(self):
        self.__pool_handler()
        return self.output
      

if __name__ == '__main__':
    from time import time
    
    def complex_math(n):
        return (66*n // (1 + n**2)) + (n**8 / (3*n**3 + 1))  
    
    data = [i for i in range(10_000_000)]
    
    start = time()

    test = [complex_math(i) for i in data]
    basic = time()

    stack = parallelogram(data, complex_math).run_stack()
    multi = time()

    print(
        f'Base: {round(basic - start, 1)}s\nParallel: {round(multi - basic, 1)}s'
    )
    pct = 100 * ((basic - start) - (multi - basic)) / (basic - start) 
    print(f'Time reduction {round(pct, 1)}%')

    '''OUTPUT
        Base: 12.7s
        Parallel: 4.4s
        Time reduction 65.3%
    '''