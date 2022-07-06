# ARC Survival Curves

# Import dependencies
import pandas as pd

from numpy import array, append, divide, random
from ARC_Functions import survival_probability

random.seed(0)

'''
NOTES:

- Code written in Python 3.9.10 + NumPy 1.22.3 + Pandas 1.4.2

'''

class SurvivalCurves:
    '''
        This class calculated the survival probability for a normal distribution over a user defined numbre of years. 
    '''
    
    def __init__(self, df, n_years, age_mean_col, age_mean_stdev_col):
        self.df = df
        self.years = [i for i in range(n_years)]
        self.samples = 100

        self.base = array([])
        self.cond = array([])

        self.ages = array([0 for i in df.index])
        self.means = df[age_mean_col].to_numpy()
        self.devs = df[age_mean_stdev_col].to_numpy()
        self.iters = range(len(self.ages))

 
    def __base_probability(self):
        '''
            Generates the survival probability at the base age array value.
        '''
        self.base = array([survival_probability(self.ages[i], self.means[i], self.devs[i], self.samples) for i in self.iters])


    def __conditional_probability(self):
        '''
            Calculates the conditional survival probability at a given age.
        '''
        # Probability for current age
        p_a = array([survival_probability(self.ages[i] + self.years[0], self.means[i], self.devs[i], self.samples) for i in self.iters])

        # Probability of survival max
        p_b = self.base
        
        # Probability of survival to previous age
        if self.years[0] == 0:
            p_ba = self.base
        else: 
            p_ba = array([survival_probability(self.ages[i] + self.years[0] - 1, self.means[i], self.devs[i], self.samples) for i in self.iters])

        # calculate conditional probability and update array
        for i in self.iters:
            if p_b[i] == 0:
                result = 0
            else:
                result = divide(p_a[i] * p_ba[i], p_b[i])        
            self.cond = append(self.cond, result)

    def generate(self):
        '''
            Runs the ARC class using to generate survival probability forcasts from zero to n_years.
        '''
        # initialise base probability in memory and assign to year_0
        self.__base_probability()
        self.df['year_0'] = self.base

        # Iterate over self.years
        for i in range(len(self.years)):
            self.__conditional_probability()
            
            self.df[f'year_{i + 1}'] = self.cond

            self.years.pop(0) # remove year from list
            self.cond = array([]) # re-initialise empty array
            self.df = self.df.copy() # stablise df 
        
        return self.df


if __name__ == '__main__':
    from time import time
    
    # if taking a cut of the df - remember to reset_index(drop = True)
    df = pd.read_csv(r'data/2021_inv_model.csv')
    print(f'Rows : {df.shape[0]}')
    
    # Time run
    start = time()
    df_out = SurvivalCurves(
        df.copy(), 
        n_years=100, 
        age_mean_col = 'mean_life', 
        age_mean_stdev_col = 'stdev'
        ).generate()

    print(f'Run complete : {round((time() - start) / 60, 1)} min')