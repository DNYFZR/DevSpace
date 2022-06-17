# Library class orchestrator
import datetime as dt
def arrayed(x):
    from .__functions import random_int_array
    return random_int_array(n_high = x, n_vals = x)

def carbon_api(area, start_date = dt.date(2022,6,1), end_date = dt.date(2022,6,7)):
    from .__api import carbon_data
    return carbon_data(start_date, end_date, nation=area).run_pipeline()

