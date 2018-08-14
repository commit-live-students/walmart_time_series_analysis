import pandas as pd
import datetime
from dateutil.relativedelta import *
import itertools

from greyatomlib.walmart_time_series_analysis.q04_model_data.build import q04_model_data, q03_parameter_selection, q01_preprocessing

train_df = pd.read_csv("data/train.csv")
df = q01_preprocessing(train_df)
p = d = q = range(0, 2)
#paramter combinations
pdq = list(itertools.product(p, d, q))
#for seasonal
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
pdq,s_pdq=q03_parameter_selection(df,pdq,seasonal_pdq)     

RMSE,model=q04_model_data(df,pdq,s_pdq)



def q05_predict_data(df,model):
    start = datetime.datetime.strptime("2012-11-01", "%Y-%m-%d")
    date_list = [start + relativedelta(months=x) for x in range(0,12)]
    future = pd.DataFrame(index=date_list, columns= df.columns)
    df = pd.concat([df, future])
    
    df['forecast'] = model.predict(start=pd.to_datetime('2012-10-01'),end=pd.to_datetime('2013-10-01') ,dynamic= True)  
    #print(df.tail())
    df[['Weekly_Sales', 'forecast']].plot(figsize=(12, 8)) 
    
    
    
q05_predict_data(df, model)    