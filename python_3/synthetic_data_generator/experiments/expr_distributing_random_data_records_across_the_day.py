# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:14:12 2020

@author: Ashish
"""

import numpy as np
import pandas as pd

#total number of observations:
limit = 10**2
N = 100

#percent of transactions during that hour.
weights_per_hour= (np.array([.35, .25, .25, .15])*limit).astype(int)

#generate time range using Pandas datetime functions
time_range = pd.date_range(start = '20201001',freq='H', periods=4)

#generate data index according to the hour distribution.
time_indx  = time_range.repeat(weights_per_hour)

#create temp data frame as a housing unit.
dat_dict =  {"t_id":[x+100 for x in range(N)], "transaction_date":time_indx}
temp_df = pd.DataFrame(dat_dict)
print(temp_df)
