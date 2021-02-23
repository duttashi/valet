# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 07:50:11 2020
Objective: Given a location list as input to a function, 
randomly shuffle and repeat the location list N number of times
Function parameters: location list, number of repetitions
Function return value: random shuffled list of locations
@author: Ashish
"""
import random

def random_shuffled_locations(loc_list,num):
    rand_shuf_str = [item for item in loc_list for i in range(num)]
    random.shuffle(rand_shuf_str)
    return(rand_shuf_str)

# implementation
lst = ['pj','selangor','kl','cheras','ttdi']
n=10
rand_loc_lst = random_shuffled_locations(lst, n)
print(rand_loc_lst)
print("list size: ", len(rand_loc_lst))