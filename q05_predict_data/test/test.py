
import pandas as pd
#import sys,os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q05_predict_data
from greyatomlib.walmart_time_series_analysis.q04_model_data.build import q04_model_data,q03_parameter_selection, q01_preprocessing
import itertools
from inspect import getfullargspec


train_df = pd.read_csv("data/train.csv")
df = q01_preprocessing(train_df)
p = d = q = range(0, 2)
#paramter combinations
pdq = list(itertools.product(p, d, q))
#for seasonal
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
pdq,s_pdq=q03_parameter_selection(df,pdq,seasonal_pdq)     

RMSE,model=q04_model_data(df,pdq,s_pdq)
q05_predict_data(df,model)

class TestParam2(TestCase):
    def test_param2_args(self):

        # Input parameters tests
        args = getfullargspec(q05_predict_data)
        self.assertEqual(len(args[0]), 2, "Expected argument(s) %d, Given %d" % (2, len(args[0])))
     
   