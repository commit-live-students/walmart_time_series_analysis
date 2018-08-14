
import pandas as pd
#import sys,os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q02_stationarity
from greyatomlib.walmart_time_series_analysis.q01_preprocessing.build import q01_preprocessing
from inspect import getfullargspec


train_df = pd.read_csv("data/train.csv")
df = q01_preprocessing(train_df)

q02_stationarity(df)

class TestParam2(TestCase):
    def test_param2_args(self):

        # Input parameters tests
        args = getfullargspec(q02_stationarity)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))
     
   