import pandas as pd
import numpy as np
import statsmodels.api as sm
import itertools

from greyatomlib.walmart_time_series_analysis.q03_parameter_selection.build import q03_parameter_selection,q01_preprocessing

train_df = pd.read_csv("data/train.csv")
df = q01_preprocessing(train_df)

# Parameter initialization for the model
p = d = q = range(0, 2)

#'order' paramter combination 
pdq = list(itertools.product(p, d, q))

#'seasonal_order' parameter combination for seasonal
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

pdq_element, s_pdq_element=q03_parameter_selection(df,pdq,seasonal_pdq)     




