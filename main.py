import csv
import re

with open('details.csv', 'r', encoding='utf-8') as f:
    file=csv.reader(f)
    for row in file:
        x = re.search(r'(?P<publihserlocation>\w+)(\s:\s)(?P<publishername>\w+(.*?)),\s(?P<publisheryear>\d+)',row[0])
        y = re.search(r'(\d{4},\s)*((vol.|t.|Vol.|.vol.|T.)\s(?P<vol>\d+))*(,\s)*((iss.|nr|no.|No.|num.|Nr|Issue)\s(?P<no>\d+))*((s.\s|S.\s)(?P<pagesinrange>\d+-\d+))*((nr\sart.\s)(?P<articleno>[a-z]\d+))*', row[1])
        #print(x.group('locationname'))
        print(y.group('articleno'))

#https://regex101.com/r/C53N5j/1