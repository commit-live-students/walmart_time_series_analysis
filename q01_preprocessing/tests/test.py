import pandas as pd
from unittest import TestCase
from ..build import q01_preprocessing
from inspect import getfullargspec

train_df = pd.read_csv("data/train.csv")
df = q01_preprocessing(train_df)
#df1=test_func(train_df)

class TestParam2(TestCase):
    def test_param2_args(self):

        # Input parameters tests
        args = getfullargspec(q01_preprocessing)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))


    def test_df_shape(self):
        self.assertEqual(df.shape, (33, 7) ,"Expected shape does not match given shape")
    
    def test_store_values(self):
        values = df['Store'].value_counts().keys().tolist()[0]
        self.assertEqual(values, 1.0 ,"You haven't subsetted the data based on Store")

    def test_store_count(self):
        counts = df['Store'].value_counts().tolist()[0] 
        self.assertEqual(counts, 33 ,"You haven't subsetted the data based on Store")
 
     