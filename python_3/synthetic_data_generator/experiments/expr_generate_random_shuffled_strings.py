# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:44:53 2020
Objective: Given a predefined list of strings, and a number
generate random repetitions of the list of strings equivalent to the number.
Suppose, the list has 5 items and I want a new list 
having N number of list items with repetitions.
@author: Ashish
"""
import random
# define a list of advert types
ad_type = ['baby product','kitchenware','electronics','mobile phones','laptops']
ad_screen_loc = ['cheras','universiti','sungai besi','ampang','kl sentral']
ad_screen_coords = [(1121, 6), (1807, 2315), (1255, 1234), (1777, 1789), (611, 986)]

# randomly shuffle the obkects in list
random.shuffle(ad_type)
# print(ad_type)
# x = [random.random() for x in range(100)]
# print(x)
# repeat list items
n=3
ad_type_repeat = [item for item in ad_type for i in range(n)]
random.shuffle(ad_type_repeat)
# print(ad_type_repeat)

def random_shuffled_strings(num, str_lst):
    n = num
    lst = str_lst
    rand_shuf_str = [item for item in lst for i in range(n)]
    random.shuffle(rand_shuf_str)
    return(rand_shuf_str)

# implementation
x = random_shuffled_strings(10,ad_screen_loc)
print(x)
    