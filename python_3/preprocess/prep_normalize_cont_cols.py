# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 14:13:03 2021
Function: normalise the continuous variables
Input parameter: dataframe
Output: normalised cols
@author: Ashish
"""

from sklearn.preprocessing import MinMaxScaler

def normalize_col(data):
    for col in testing.columns.values.tolist():
        scaler = MinMaxScaler()
        data[col] = scaler.fit_transform(data[col].values.reshape(-1,1))
    return data

