# Library class orchestrator
import datetime as dt

class pyDev:
    def __init__(self):
        pass
    
    @staticmethod
    def arrayed(x):
        from functions import random_int_array
        return random_int_array(n_high = x, n_vals = x)

    @staticmethod
    def carbon_api(area, start_date = dt.date(2022,6,1), end_date = dt.date(2022,6,7)):
        from api import carbon_data
        return carbon_data(start_date, end_date, nation=area).run_pipeline()


if __name__ == '__main__':
    api_call = pyDev.carbon_api('Scotland')
