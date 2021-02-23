# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 07:50:11 2020
Objective: Given a product list as an input to a function, 
randomly shuffle and repeat the list N number of times
Function parameters: product list, number of repetitions
Function return value: random shuffled list of products
@author: Ashish
"""
import random

def random_shuffled_products(loc_list,num):
    rand_shuf_str = [item for item in loc_list for i in range(num)]
    random.shuffle(rand_shuf_str)
    return(rand_shuf_str)

# implementation
lst = ['soft toys','kitchenware','electronics','mobile phones','laptops']
n=10
rand_loc_lst = random_shuffled_products(lst, n)
print(rand_loc_lst)
print("list size: ", len(rand_loc_lst))