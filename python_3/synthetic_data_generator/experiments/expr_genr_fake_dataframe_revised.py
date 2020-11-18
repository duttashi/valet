# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 08:22:32 2020

@author: Ashish
"""
import random
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# function: given a list of locations, assign locations randomly 
def rand_shuf_loc(loc_lst,rows_num):
    lst = loc_lst
    # using list comprehension
    rand_shuf_str = [item for item in lst for i in range(rows_num)]
    random.shuffle(rand_shuf_str)
    return(rand_shuf_str)
    # return(x)

# function: given a list of product names, assign products randomly
def rand_shuf_prod(prod_list,rows_num):
    rand_shuf_str = [item for item in prod_list for i in range(rows_num)]
    random.shuffle(rand_shuf_str)
    return(rand_shuf_str)

# function: given a list of product names, generate random product price and discount

def rand_prod_price_discount(adv_prod, rows_num):
    prod_price_lst = []  # advertised product price
    prod_discnt_lst = []  # advertised product discount
    for item in adv_prod:
        for i in range(rows_num):
            prod_price_lst.append(random.randint(10, 100))
            prod_discnt_lst.append(random.randint(10, 100))
    return {'prod_price_lst': prod_price_lst,
            'prod_discnt_lst': prod_discnt_lst}

# function: given a list of product names, generate random clicks and impressions
def rand_clic_impr(adv_prod, rows_num):
    rand_impr_lst = []
    click_lst = []
    for item in adv_prod:
        for i in range(rows_num):
            rand_impr_lst.append(random.randint(0, 100))
            click_lst.append(random.randint(0, 100))
    return {'rand_impr_lst': rand_impr_lst, 'rand_click_lst': click_lst}

def randomTime(adv_prod, rows_num):
    # generate random number scaled to number of seconds in a day
    # (24*60*60) = 86,400
    time_list = []
    for item in adv_prod:
        for i in range(rows_num):
            rtime = int(random.random()*86400)
            hours = int(rtime/3600)
            minutes = int((rtime - hours*3600)/60)
            seconds = rtime - hours*3600 - minutes*60
            time_string = '%02d:%02d:%02d' % (hours, minutes, seconds)
            time_list.append(time_string)
    return {'time_list': time_list}

def randomDate(start_date, end_date, adv_prod, rows_num):
    date_list = []
    for item in adv_prod:
        for i in range(rows_num):
            random_date = np.random.choice(pd.date_range(start_date, end_date, freq = 'M'))
            # print(random_date)
            date_list.append(random_date)
    return {'date_list': date_list}

# function: given a list of product names, assign products randomly
def rand_shuf_adsize(adv_size,rows_num):
    rand_shuf_str = [item for item in adv_size for i in range(rows_num)]
    random.shuffle(rand_shuf_str)
    return(rand_shuf_str)

def main():
    # declare global variables
    adv_loc = ['cheras', 'universiti', 'sungai besi',
           'ampang', 'kl sentral']
    adv_prod = ['baby product', 'kitchenware', 'electronics',
            'mobile phones', 'laptops']
    adv_size = [1, 2, 3, 4, 10]
    # adv_layout = ['static', 'dynamic']
    rows_num = 10  #the given dimension
    start_date = "2020-1-1" # year-month-day format
    end_date = "2020-12-31"
    print('generating data...')
    impression = rand_clic_impr(adv_prod,rows_num)
    clicks = rand_clic_impr(adv_prod,rows_num)
    product_price = rand_prod_price_discount(adv_prod,rows_num)
    product_discount = rand_prod_price_discount(adv_prod,rows_num)
    prod_clik_tmstmp = randomTime(adv_prod,rows_num)
    prod_clik_datestmp = randomDate(start_date, end_date,adv_prod,rows_num)
    # create a dictionary of the lists above
    lst_dict = {"ad_loc": rand_shuf_loc(adv_loc,rows_num),
                "prod": rand_shuf_prod(adv_prod,rows_num),
                "adv_size": rand_shuf_adsize(adv_size,rows_num),
                "imprsn": impression['rand_impr_lst'],
                "cliks": clicks['rand_click_lst'],
                "prod_price": product_price['prod_price_lst'],
                "prod_discnt": product_discount['prod_discnt_lst'],
                "prod_clik_timestmp": prod_clik_tmstmp['time_list'],
                "prod_clik_datestmp": prod_clik_datestmp['date_list']
                }
    fake_data = pd.DataFrame.from_dict(lst_dict, orient="index")
    result = fake_data.transpose()
    print(result)
    result.to_csv("../../../data/fake_data.csv", sep=",")

# invoke the main function


if __name__ == "__main__":
    main()