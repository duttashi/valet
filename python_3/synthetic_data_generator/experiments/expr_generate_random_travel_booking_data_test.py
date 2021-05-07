# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 22:40:55 2021

@author: Ashish
"""
import pandas as pd
import random, re
import numpy as np
TRIPTYPE = ['apple','orange','guava']
ORIG = ['KUL','IND']
# ORIG = ["KUL","IND","AUS","CHN","USA","UK"]
ROW_COUNT = 5 # denotes number of rows 

def get_airport_orig():
    # a = 'KULAMRJPNINDRUSPENKULNPLSGRUSA'
    # lst = [str[i:i+3] for i in range(0, len(a), 3)]
    # lst_orig = re.findall(".{3}", ORIG)
    
    # improve this function by generating 3 character words N number of times
    # lst_orig = ['KUL','AMR','BGLR','NDL','PEN','JPN','IND','NPL','AUS','UK']
    random.shuffle(ORIG)
    return ORIG
    
def get_random_triptype():
    random.shuffle(TRIPTYPE)
    # print(lst_triptype)
    return TRIPTYPE

lst_triptype = get_random_triptype()
lst_airprt_orig = get_airport_orig()

df = pd.DataFrame.from_dict({
                       "orig": lst_airprt_orig,
                       "trip_type":lst_triptype,
                       }, orient='index').T
df_expanded = df.loc[np.repeat(df.index.values,ROW_COUNT)]

# print(df)
# print(df_expanded)

# Now randomly shuffle the rows
# reference: https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows
df_expanded = df_expanded.sample(frac=1).reset_index(drop=True)
print(df_expanded)
