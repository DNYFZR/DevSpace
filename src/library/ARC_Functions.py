# ARC Functions
from functools import lru_cache
from numpy import array, mean, random
import pandas as pd


@lru_cache(maxsize=None)
def survival_probability(age_model, age_mean, age_stdev, n_samples=1000, n_seed=0):    
    '''
        Calculates a survivial probability curve using a normal distribution of n_samples.
    '''
    random.seed(n_seed)
    p_dist = array(random.normal(age_mean, age_stdev, n_samples))
    return mean([1 if j - age_model >= 0 else 0 for j in p_dist])


@lru_cache(maxsize=64)
def simulate_survival(p_survival, n_seed=0):
    '''
        Runs a comparison of p_survival to p_random. 
        If p_survival >= p_random then return 1 (survived) else 0 (failed)
    '''
    random.seed(n_seed)
    if p_survival >= random.random():
        return 1
    else:
        return 0


@lru_cache(maxsize=128)
def simulate_survival_2(p_survival, n_seed=0, n_sim = 10000):
    '''
        Runs a comparison of p_survival to p_random. 
        If p_survival >= p_random then return 1 (survived) else 0 (failed)
    '''
    random.seed(n_seed)
    p_mean = mean([1 if p_survival >= random.random() else 0 for _ in range(n_sim)])

    if p_mean >= 0.5:
        return 1
    else:
        return 0


def dataframe_chunker(df, chunk_len):
    '''
        Creates a chunk generator object from a dataframe of n_chunks length. 
    '''
    for i in range(0, len(df), chunk_len):
        yield df.iloc[i:i+chunk_len, :].copy()



def dataframe_unchunker(df_generator):
    '''
        Takes a dataframe chunk generator object and returns a unified dataframe.    
    '''
    output = pd.DataFrame()
    for chunk in list(df_generator):
        output = pd.concat([output.copy(), chunk], axis=0)
    
    return output