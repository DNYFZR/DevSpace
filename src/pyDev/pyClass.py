########################################
###### Library class orchestrator ######
########################################

import datetime as dt

class pyClass:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def arrayed(x):
        from functions import random_int_array
        return random_int_array(n_high = x, n_vals = x)

    @staticmethod
    def carbon_api(area, start_date = dt.date(2022,4,12), end_date = dt.date(2022,4,20)):
        from api import carbon_data
        return carbon_data(start_date, end_date, nation=area).run_pipeline()

    @staticmethod
    def parallel_processor(data, applied_function):
        from parallelogram import parallelogram
        return parallelogram(input_data=data, process_function=applied_function).run_stack()

if __name__ == '__main__':
    def tester(x): 
        return x**2 / x**3

    test = pyClass.arrayed(100)

    # test2 = pyClass.carbon_api('Scotland')
   
    test3 = pyClass.parallel_processor(test, tester)