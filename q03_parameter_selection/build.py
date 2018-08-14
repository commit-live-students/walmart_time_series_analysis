import pandas as pd

from greyatomlib.walmart_time_series_analysis.q01_preprocessing.build import q01_preprocessing

train_df = pd.read_csv("data/train.csv")
df = q01_preprocessing(train_df)

import statsmodels.api as sm
import itertools

p = d = q = range(0, 2)

#paramter combinations
pdq = list(itertools.product(p, d, q))

#for seasonal
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

#print('Examples of parameter combinations for Seasonal ARIMA...')
#print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
#print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
#print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
#print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))


def q03_parameter_selection(df, pdq,s_pdq):
    AIC_Score=10000000000000000
    y=df['Weekly_Sales']
    for param in pdq:

        for param_seasonal in s_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(y[:'2011-02-01'],
                                                order=param,
                                                seasonal_order=param_seasonal,
                                                enforce_stationarity=False,
                                                enforce_invertibility=False)

                results = mod.fit()
                if results.aic<AIC_Score:
                    AIC_Score=results.aic
                    P=param
                    Q=param_seasonal
                #print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
            except:
                continue
                
    return P,Q


pdq,s_pdq=q03_parameter_selection(df,pdq,seasonal_pdq)     
print(pdq,s_pdq)