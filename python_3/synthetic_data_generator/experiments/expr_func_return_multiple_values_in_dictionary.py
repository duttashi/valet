# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:25:30 2020
write a function that returns a dictionary of multiple values.
Then unpack the return dictionary values
@author: Ashish
"""

import random
num=10
# geerate random impression and click data
def rand_click_impression_data(num):
    rand_impr_lst = []
    click_lst = []
    for i in range(num):
        rand_impr_lst.append(random.randint(0, 100))
        click_lst.append(random.randint(0, 50))
    return {'rand_impr_lst': rand_impr_lst, 'rand_click_lst': click_lst}
impr_data = rand_click_impression_data(num)
click_data = rand_click_impression_data(num)
# print(rand_impr(num))
print(impr_data['rand_impr_lst'])
print("\n####")
print(click_data['rand_click_lst'])