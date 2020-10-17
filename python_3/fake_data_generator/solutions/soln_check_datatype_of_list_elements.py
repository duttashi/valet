# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 11:26:36 2020
The given function returns the data type of a list object passed to it
@author: Ashish
"""
def checkType(a_list):
    for element in a_list:
        if isinstance(element, int):
            print("It's an Integer")
        if isinstance(element, str):
            print("It's an string")
        if isinstance(element, float):
            print("It's an floating number")
            
# Test run
mylist = [1,2,3,4,"abc"]
print(checkType(mylist))

