import pandas as pd
import numpy as np
import statsmodels.api as sm
import itertools

from greyatomlib.walmart_time_series_analysis.q03_parameter_selection.build import q03_parameter_selection,q01_preprocessing

train_df = pd.read_csv("data/train.csv")
df = q01_preprocessing(train_df)
p = d = q = range(0, 2)
#paramter combinations
pdq = list(itertools.product(p, d, q))
#for seasonal
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
pdq,s_pdq=q03_parameter_selection(df,pdq,seasonal_pdq)     


def q04_model_data(df,pdq,s_pdq):
    y=df['Weekly_Sales']
    mod = sm.tsa.statespace.SARIMAX( y[:'2011-02-01'],
                                order=pdq,
                                seasonal_order=s_pdq,
                                enforce_stationarity=False,
                                enforce_invertibility=False)

    results = mod.fit()
    pred = results.get_prediction(start=pd.to_datetime('2011-03-01'),end=pd.to_datetime('2012-10-01'), dynamic=False)
    y_forecasted = pred.predicted_mean
    y_truth = y['2011-02-01':]
    # Compute the mean square error
    mse = ((y_forecasted - y_truth) ** 2).mean()
    
    return np.sqrt(mse), results
    
#print(q04_model_data(df,pdq,s_pdq))


