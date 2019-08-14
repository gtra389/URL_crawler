import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np

r = requests.get('http://ec2-54-175-179-28.compute-1.amazonaws.com/get_info_extra.php')
soup = BeautifulSoup(r.text,'lxml')
a = list(soup.find_all('p'))

# Split the list through the regular expression
d = re.split('\s+|,,|:,',str(a))

# Remove the '' element from the list
d = list(filter(lambda zz: zz != '', d)) 

# Remove the '=' element from the list
d = list(filter(lambda zz: zz != '=', d))

# Create a dataframe
colName=['id', 'time', 'weather', 'air', 'acc']
_Num = 0
_df  = pd.DataFrame(columns=colName)
df   = pd.DataFrame(columns=colName)

for ii in range(0,len(d)):    
    while colName[_Num] in d[ii]:
        _lst = d[ii + 1]
        _lst = _lst.strip(',')
        
        if _lst == '' or (_lst in colName):
            _lst = None       
        
        _df[colName[_Num]] = [_lst] # Put the list into the dataframe
        if _Num < (len(colName)-1):
            _Num += 1
        else:
            df = df.append(_df, ignore_index=True)
            _Num = 0 

df.to_csv('Result.csv')  
