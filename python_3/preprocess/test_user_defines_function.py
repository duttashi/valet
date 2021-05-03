# -*- coding: utf-8 -*-
"""
Created on Mon May  3 11:20:27 2021

@author: Ashish
"""

from python_3.preprocess.normalize_data import *

# create some dummy data
alist = [10,22,9,34,12]

# test the normalisation function
print(normalization([2, 7, 10, 20, 30, 50]))
print(normalization(alist))