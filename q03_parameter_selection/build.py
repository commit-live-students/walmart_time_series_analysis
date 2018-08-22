import pandas as pd

import statsmodels.api as sm
import itertools

from greyatomlib.walmart_time_series_analysis.q01_preprocessing.build import q01_preprocessing

train_df = pd.read_csv("data/train.csv")
df = q01_preprocessing(train_df)

# Parameter initialization for the model
p = d = q = range(0, 2)

#'order' paramter combination 
pdq = list(itertools.product(p, d, q))

#'seasonal_order' parameter combination for seasonal
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

def q03_parameter_selection(df, pdq,seasonal_pdq):
    
#    AIC_Score=10000000000000000
#    y=df['Weekly_Sales']

# To iterate through all the possible parameter combinations of 'order' and 'seasonal_order'     
    for param in pdq:

        for param_seasonal in s_pdq:
#While feeding the model, different parameter combinations, exceptions might get thrown for certain combinations            
            try:
            """ Write your code for finding the parameter combination with the lowest AIC score"""
            except:
                continue
    
    """ Return the pdq and s_pdq assosicated with lowest AIC here """            
#    return ... 

