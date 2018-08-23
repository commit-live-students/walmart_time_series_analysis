import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from collections import OrderedDict
plt.switch_backend('agg')
%matplotlib inline


from greyatomlib.walmart_time_series_analysis.q01_preprocessing.build import q01_preprocessing

train_df = pd.read_csv("data/train.csv")
df = q01_preprocessing(train_df)
