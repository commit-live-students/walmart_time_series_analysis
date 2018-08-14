import pandas as pd

train_df = pd.read_csv("data/train.csv")

def q01_preprocessing(df):
    "write your solution here"
    df = df.copy()
    df.Date =pd.to_datetime(df.Date,format='%Y-%m-%d')
    df['Year'] = pd.DatetimeIndex(df['Date']).year
    df['Month'] = pd.DatetimeIndex(df['Date']).month
    df['Day'] = pd.DatetimeIndex(df['Date']).day
    df=df.set_index('Date')
    df.index = pd.to_datetime(df.index)
    df=df[df['Store']==1]
    df_mean = df.resample('MS').mean()
    return df_mean

 
