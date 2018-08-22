
import pandas as pd
#import sys,os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q03_parameter_selection
from greyatomlib.walmart_time_series_analysis.q01_preprocessing.build import q01_preprocessing

from inspect import getfullargspec


train_df = pd.read_csv("data/train.csv")
df = q01_preprocessing(train_df)

import itertools

p = d = q = range(0, 2)

#paramter combinations
pdq = list(itertools.product(p, d, q))

#for seasonal
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

pdq,s_pdq=q03_parameter_selection(df,pdq,seasonal_pdq)     

class TestParam2(TestCase):
    def test_param2_args(self):

        # Input parameters tests
        args = getfullargspec(q03_parameter_selection)
        self.assertEqual(len(args[0]), 3, "Expected argument(s) %d, Given %d" % (3, len(args[0])))


    def test_pdq(self):
        self.assertEqual(pdq, (0,0,0), "The Expected values do not match with the Returned value")
        
    
    def test_seasonal_pdq(self):
        self.assertEqual(s_pdq, (1,0,0,12), "The Expected values do not match with the Returned value")
        
        