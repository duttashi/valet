# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:06:34 2020
See script expr_generate_random_shuffled_strings.py
This function will take a list of strings and number of repetitions as input
It will generate a list of repeated strings
@author: Ashish
"""
import random

def random_shuffled_strings(num, str_lst):
    n = num
    lst = str_lst
    # using list comprehension
    rand_shuf_str = [item for item in lst for i in range(n)]
    random.shuffle(rand_shuf_str)
    return(rand_shuf_str)

# implementation
ad_screen_loc = ['pj','selangor','kl','cheras','ttdi']
x = random_shuffled_strings(10,ad_screen_loc)
print(x)

