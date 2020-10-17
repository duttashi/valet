# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:25:12 2020

@author: Ashish
"""

import random
import pandas as pd
num = 20

def rand_clic_impr(num):
    rand_impr_lst = []
    click_lst = []
    for i in range(num):
        rand_impr_lst.append(random.randint(0, 100))
        click_lst.append(random.randint(0, 100))
    return {'rand_impr_lst': rand_impr_lst, 'rand_click_lst': click_lst}

# define function to generate random product price and discount
def rand_prod_price_discount(num):
    prod_price_lst = []  # advertised product price
    prod_discnt_lst = []  # advertised product discount
    
    for i in range(num):
        prod_price_lst.append(random.randint(10, 100))
        prod_discnt_lst.append(random.randint(10, 100))
    
    return {'prod_price_lst': prod_price_lst, 'prod_discnt_lst': prod_discnt_lst}

# generate random coordinates
def rand_coord(num):
    cord_lst = [(random.random()*2.0, random.random()*2.0) for _ in range(num)]
    return {'geo_cord_lst': cord_lst}
    
def main():
    print('generating data...')
    # print('generating random geographic coordinates...')
    # get the impressions and click data
    impression = rand_clic_impr(num)
    clicks = rand_clic_impr(num)
    product_price = rand_prod_price_discount(num)
    product_discount = rand_prod_price_discount(num)
    geo_cord = rand_coord(num)
    # print("pp: ", product_price)
    # start = rand_shuf_date('2010-10-1', '2010-10-30', 10)
    # end = rand_shuf_date('2010-10-1', '2010-10-30', 10)
    # add all lists to a dictionary
    # lst_dict = {"geog_cord": rand_geog_cord(num),
    #             "ad_loc": rand_shuf_loc(adv_loc, num),
    #             "ad_prod": rand_shuf_prod(adv_prod, num),
    #             "impressions": impression['rand_impr_lst'],
    #             "clicks": clicks['rand_click_lst']}
    lst_dict = {"impressions": impression['rand_impr_lst'],
                "clicks": clicks['rand_click_lst'],
                "prod_price": product_price['prod_price_lst'],
                "prod_discnt": product_discount['prod_discnt_lst'],
                "geo_cord": geo_cord['geo_cord_lst']}
    fake_data = pd.DataFrame.from_dict(lst_dict, orient="index")
    # fake_data = pd.DataFrame(fake_data)
    # print("Fake dataset\n", fake_data.transpose())
    
    # check if var is a pandas dataframe
    # if isinstance(fake_data, pd.DataFrame):
    #     print("fake_data is a pandas dataframe")
    # else:
    #     print("Not a dataframe. Its type is: ", type(fake_data))
    
    #  filling none with random numbers pandas dataframe columns
    res = fake_data.apply(lambda x: x.fillna(0)
                          if x.dtype.kind in 'biufc'
                          # where 'biufc' means boolean, integer,
                          # unicode, float & complex data types
                          else x.fillna(random.randint(0, 100)
                                        )
                          )
    print(res.transpose())

# invoke the main function


if __name__ == "__main__":
    main()
    