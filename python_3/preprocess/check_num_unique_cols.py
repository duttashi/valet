# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 14:07:43 2021
Function: to check number of unique columns
Input parameter: dataframe
Output: none
@author: Ashish
"""

'''Find and count the number of non-unique columns'''

def nunique_counts(data):
   for i in data.columns:
       count = data[i].nunique()
       print(i, ": ", count)