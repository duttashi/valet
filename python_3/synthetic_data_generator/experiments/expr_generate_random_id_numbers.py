# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 08:10:33 2020

@author: Ashish
"""
import random, string
n=10
def generate_random_id_numbers() -> list:
    """ Generate dummy Health Service ID numbers similar to NHS 10 digit format
    See: https://www.nhs.uk/using-the-nhs/about-the-nhs/what-is-an-nhs-number/
    """
    DA_id_numbers = []
    for _ in range(n): 
        DA_id = ''.join(random.choice(string.digits) for _ in range(3)) + '-'   
        DA_id += ''.join(random.choice(string.digits) for _ in range(3)) + '-'   
        DA_id += ''.join(random.choice(string.digits) for _ in range(4))
        DA_id_numbers.append(DA_id)
    return DA_id_numbers

x = generate_random_id_numbers()
print(x)
print("length: ", len(x))