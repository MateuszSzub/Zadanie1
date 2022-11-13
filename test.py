import pandas as pd
import unittest
from pandas.testing import assert_frame_equal

class TestOperations(unittest.TestCase):

    def setUp(self):
        global dfo, dfd
        dfo = pd.read_csv('output.csv', header=None,names=['no', 'vol', 'articleno', 'pagesinrange', 'publishername', 'publisherlocation','publisheryear'], dtype={'no': 'object', 'articleno': 'object'}, delimiter=',')
        dfd = pd.read_csv("details.csv", header=None, usecols=[2, 3, 4, 5, 7, 8, 9],names=['no', 'vol', 'articleno', 'pagesinrange', 'publishername', 'publisherlocation','publisheryear'], delimiter=',')

    def testCol(self):
        col_output = len(dfo.columns)
        col_details = len(dfd.columns)
        self.assertEqual(col_output, col_details)

    def testRow(self):
        row_output = len(dfo)
        row_details = len(dfd)
        self.assertEqual(row_output, row_details)

    def testHead(self):
        output_value = dfo.head(1)
        details_value = dfd.head(1)
        assert_frame_equal(output_value, details_value)

    def testNo(self):
        dfno1 = pd.DataFrame()
        dfno1['no'] = dfo['no']
        dfno2 = pd.DataFrame()
        dfno2['no'] = dfd['no']
        assert_frame_equal(dfno1, dfno2)

    def testVol(self):
        dfvol1 = pd.DataFrame()
        dfvol1['vol'] = dfo['vol']
        dfvol2 = pd.DataFrame()
        dfvol2['vol'] = dfd['vol']
        assert_frame_equal(dfvol1, dfvol2)

    def testArticleno(self):
        dfart1 = pd.DataFrame()
        dfart1['articleno'] = dfo['articleno']
        dfart2 = pd.DataFrame()
        dfart2['articleno'] = dfd['articleno']
        assert_frame_equal(dfart1, dfart2)

    def testPagesinrange(self):
        dfpr1 = pd.DataFrame()
        dfpr1['pagesinrange'] = dfo['pagesinrange']
        dfpr2 = pd.DataFrame()
        dfpr2['pagesinrange'] = dfd['pagesinrange']
        assert_frame_equal(dfpr1, dfpr2)

    def testPublishername(self):
        dfpn1 = pd.DataFrame()
        dfpn1['publishername'] = dfo['publishername']
        dfpn2 = pd.DataFrame()
        dfpn2['publishername'] = dfd['publishername']
        assert_frame_equal(dfpn1, dfpn2)

    def testPublisherlocation(self):
        dfpl1 = pd.DataFrame()
        dfpl1['publisherlocation'] = dfo['publisherlocation']
        dfpl2 = pd.DataFrame()
        dfpl2['publisherlocation'] = dfd['publisherlocation']
        assert_frame_equal(dfpl1, dfpl2)

    def testPublisheryear(self):
        dfpy1 = pd.DataFrame()
        dfpy1['publisheryear'] = dfo['publisheryear']
        dfpy2 = pd.DataFrame()
        dfpy2['publisheryear'] = dfd['publisheryear']
        assert_frame_equal(dfpy1, dfpy2)

if __name__ == '__main__':
    unittest.main()