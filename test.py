import pandas as pd
import unittest
from pandas.testing import assert_frame_equal
import numpy as np

class TestOperations(unittest.TestCase):
    def setUp(self):
        global df1, df2
        df1 = pd.read_csv('output.csv', header=None, delimiter=',')
    def test_dataFrame_1(self):
        data = {0: 1.0, 1: 9.0, 2: np.nan, 3: None, 4: 'Varazdin Development and Entrepreneurship Agency',5: 'Varazdin', 6: 2019.0}
        df2 = pd.DataFrame(data, index=[0])
        publisher_value = df1.head(1)
        details_value = df2
        #extractor = Extractor(publisher_value, details_value)
        assert_frame_equal(publisher_value, details_value)
    def test_dataFrame_2(self):
        data2 = {0: 2.0, 1: 9.0, 2: np.nan, 3: None, 4: 'Varazdin Development and Entrepreneurship Agency',5: 'Varazdin', 6: 2019.0}
        df3 = pd.DataFrame(data2, index=[0])
        publisher_value = df1.head(1)
        details_value = df3
        #extractor = Extractor(publisher_value, details_value)
        assert_frame_equal(publisher_value, details_value)
if __name__ == '__main__':
    unittest.main()