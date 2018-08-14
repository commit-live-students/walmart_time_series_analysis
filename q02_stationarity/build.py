import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from collections import OrderedDict

from greyatomlib.walmart_time_series_analysis.q01_preprocessing.build import q01_preprocessing

train_df = pd.read_csv("data/train.csv")
df = q01_preprocessing(train_df)


def q02_stationarity(df):
    "write your solution here"
    plt.plot(df['Weekly_Sales'])

    #Determing rolling statistics
    rolmean = df.rolling(window=12, center=False).mean()
    rolstd = df.rolling(window=12, center=False).std()

    #Plot rolling statistics:
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)
    
    
    #Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    tstest=adfuller(df['Weekly_Sales'], autolag='AIC')
    tsoutput = pd.Series(tstest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in tstest[4].items():
        tsoutput['Critical Value (%s)' % key] = value
    print(tsoutput)

