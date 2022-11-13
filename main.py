import pandas as pd
import re

def main():
    df=pd.read_csv("details.csv", header=None, usecols=[0, 1], names=['Column1', 'Column2'], delimiter=',')
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pattern1 = r'(?P<publisherlocation>\w+)(\s:\s)(?P<publishername>\w+(.*?)),(\s)*(?P<publisheryear>\d+)*'
    df_col1 = df['Column1'].str.extract(pattern1, flags=re.I)
    df1 = df_col1[['publishername', 'publisherlocation', 'publisheryear']]
    pattern2 = r'(\d{4},\s)?((vol.|t.|Vol.|.vol.|T.)\s(?P<vol>\d+))*(,\s)*((iss.|nr|no.|No.|num.|Nr|Issue)\s(?P<no>\d+))*(\s*)((s.\s|S.\s)(?P<pagesinrange>\d+-\d+))*((nr\sart.\s)(?P<articleno>[a-z]\d+))*'
    df_col2 = df['Column2'].str.extract(pattern2, flags=re.I)
    df2 = df_col2[['no', 'vol', 'articleno', 'pagesinrange']]
    pd.concat([df2, df1], axis=1).to_csv('output.csv', header=False, index=False)
main()
