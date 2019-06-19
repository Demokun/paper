import  numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
from sklearn import preprocessing
'''
open data file
'''
filePath = 'D:/data/example1.ct'
pf = pd.read_table(filePath,names = ['a','b','c','d','e','f'],dtype = object)
'''
delete the first line
select the "sequence"(a) column,the "base"(b) column and the "paired"(e) column 
'''
pf = pf.drop(0)
data = pd.DataFrame(pf,columns = ['a','b','e'])
'''
generate baseData(A T G C A T C G.....)
'''
baseData = pd.DataFrame(data,columns = ['b'])
'''
generate pairData(118,117,116,115,114,0,0,...)
'''
pairData = pd.DataFrame(data,columns = ['e'])
'''
select values that ">"0 convert to 1
select values that "="0 convert to 0 from pairData(118,117,116,115,0,0,...) 
and save to pairedData(1,1,1,1,0,0,...)
'''
def select(x):
    if x > 0:
        return 1
    if x == 0:
        return 0
pairData = pairData.apply(pd.to_numeric, errors="ignore")
pairedData = pairData['e'].apply(lambda x : select(x))
'''
merge data and pairedData
'''
data = pd.concat([data,pairedData],axis = 1)
data.columns = ['a','b','c','d']
'''
add one-hot columns
'''
data['m'] = 0
data['n'] = 0
data['x'] = 0
data['y'] = 0
'''
one-hot encoder
'''
data['m'].loc[data.b == 'A'] = 1
data['n'].loc[data.b == 'U'] = 1
data['x'].loc[data.b == 'G'] = 1
data['y'].loc[data.b == 'C'] = 1
'''
data rows
'''
dataRows = data.shape[0]
'''
when rows < 300 ,padding  
'''
j = dataRows
while dataRows < 300:
    paddingRow = pd.DataFrame([[j + 1 ,'N',0,0,0,0,0,0]],columns = ['a','b','c','d','m','n','x','y'])
    data = data.append(paddingRow,ignore_index = True)
    dataRows = data.shape[0]
    j = j + 1
'''
when rows > 300
'''
count = 0
if (dataRows > 300):
    while (dataRows - count * 100) > 300:
        subData = data[count * 100:count * 100 + 300]
        count += 1
    resData = data[count * 300:dataRows]
    resRows = resData.shape[0]
    i = dataRows
    while resRows < 300:
        paddingRow = pd.DataFrame([[i + 1 ,'N',0,0,0,0,0,0]],columns = ['a','b','c','d','m','n','x','y'])
        resData  = resData.append(paddingRow,ignore_index = True)
        resRows = resData.shape[0]
        i = i + 1