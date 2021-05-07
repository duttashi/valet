# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:41:17 2021
Function parameters:
    argument: dataframe with missing values
    return value: imputed data

@author: Ashish
"""
import pandas as pd
import numpy as np

# custom function
def summarize_missing(df):
    # Null counts
    s1 = df.isnull().sum().rename('No. Missing')

    s2 = pd.Series(data=[df.index[m].tolist() for m in [df[col].isnull() for col in df.columns]],
                   index=df.columns,
                   name='Index')
    # Other way, probably overkill
    #s2 = (df.isnull().replace(False, np.NaN).stack().reset_index()
    #         .groupby('level_1')['level_0'].agg(list)
    #         .rename('Index'))

    return pd.concat([s1, s2], axis=1, sort=False)

# raw data
raw_data = {'first_name': ['Jason', np.nan, 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', np.nan, 'Ali', 'Milner', 'Cooze'], 
        'age': [42, np.nan, 36, 24, 73], 
        'sex': ['m', np.nan, 'f', 'm', 'f'], 
        'preTestScore': [4, np.nan, np.nan, 2, 3],
        'postTestScore': [25, np.nan, np.nan, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'sex', 'preTestScore', 'postTestScore'])
print("data with missing values\n",df)

miss_vals = summarize_missing(raw_data)
print(miss_vals)

