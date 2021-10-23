# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 16:28:39 2021
unit test for data science
to run pytest, open command shell and type pytest scriptname.py
@author: Ashish
"""

import pandas as pd


df = pd.DataFrame({
        'colA': ['a','b','c'],
        'colB':['x','y','z'],
        'colC':['c','c','c']
        })
print(df)
def add_col(df, new_col_name, default_value):
    # add a new column with a default value
    df[new_col_name] = default_value
    
    return df

def test_add_col_passed():
    
    # setup
    df = pd.DataFrame({
        'colA': ['a','b','c'],
        'colB':['x','y','z'],
        'colC':['c','c','c']
        })
    return df

# call function
actual = add_col(df,'colD','d')
print(actual)
# set expectation
expected = pd.DataFrame({
        'colA': ['a','b','c'],
        'colB':['x','y','z'],
        'colC':['c','c','c'],
        'colD':['d','d''d']
    })

# test the function: assertion
pd.testing.assert_frame_equal(actual, expected)
