# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:35:51 2021
function to check missing data
input parameter: dataframe
output: missing data values
@author: Ashish
"""

def missing_data(data):
    total = data.isnull().sum()
    percent = (data.isnull().sum()/data.isnull().count()*100)
    tt = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    types = []
    for col in data.columns:
        dtype = str(data[col].dtype)
        types.append(dtype)
    tt['Types'] = types
    return(np.transpose(tt))