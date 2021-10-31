# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:50:39 2021

@author: Ashish
"""

from matplotlib import pyplot as plt
import math
import seaborn as sns
import pandas as pd
# create sample
df = pd.read_csv('uciml_adult.csv')

# replace all occurence of ? with NA
df1 = df.replace(to_replace='?', value=' ')
# print(df1.isnull().sum())

# describe data
print("\n Data shape: ", df1.shape)
print("\n Data types\n", df1.dtypes)

vars_cat = df1.select_dtypes(include=['object'])
vars_cont = df1.select_dtypes(include=['int64'])
print("Categorical vars",vars_cat.shape,"\n",
      "Categorical vars",vars_cont.shape)

# multiple plots in 1 page
plt.figure()
for catvar in vars_cat:
    plt.plot(catvar[0], catvar[1], label=catvar[2])
plt.legend(loc=0, frameon=False)