"""
Created on Tue Oct 13 14:50:32 2020
Revised on Oct 14 14:10 2020

Objective: To create data for click through rate prediction (CTR).
Click-through  rate  (CTR)  is  one  of  the  common  terms  in  internet
advertising  industry,
In general, internet users click on online advertising for two main reasons:
one is internet users make a targeted search,
consider ads information carefully and then click the ads;
the other is when internet users surfing on Internet.
IMPORTANT FACTORS FOR CTR
   - advertisment color, size, layout (static/dynamic),
     content size (1 line/2-5 lines/>5 lines),
     placement (right-col/left-col/top-col/bottom-col)
   - product price, discount
   - date, start time, end time

@author: Ashish
"""
import random
import pandas as pd
import time
from datetime import datetime


# declare global variables
adv_name = ['soft toys', 'kitchenware', 'electronics',
            'mobile phones', 'laptops']
adv_loc = ['cheras', 'universiti', 'sungai besi',
           'ampang', 'kl sentral']
adv_prod = ['baby product', 'kitchenware', 'electronics',
            'mobile phones', 'laptops']
adv_size = [1, 2, 3, 4, 10]
adv_layout = ['static', 'dynamic']  # advertisment layout type on website

# adv_date, start_time, end_time = []
num = 10


# define function to generate random geographic coordinates
# def rand_geog_cord(num):
#     # Generate a set of all points within 200 of the origin,
#     # to be used as offsets later
#     # There's probably a more efficient way to do this.
#     radius = 200
#     rangeX = (0, 2500)
#     rangeY = (0, 2500)
#     # qty = 100  # or however many points you want
#     deltas = set()
#     for x in range(-radius, radius+1):
#         for y in range(-radius, radius+1):
#             if x*x + y*y <= radius*radius:
#                 deltas.add((x, y))
#     randPoints = []
#     excluded = set()
#     i = 0
#     while i < num:
#         x = random.randrange(*rangeX)
#         y = random.randrange(*rangeY)
#         if (x, y) in excluded:
#             continue
#         randPoints.append((x, y))
#         i += 1
#         excluded.update((x+dx, y+dy) for (dx, dy) in deltas)
#         # print (randPoints)
#     # randPoints.apply(lambda x: x.fillna(0)
#     #                       if x.dtype.kind in 'biufc'
#     #                       # where 'biufc' means boolean, integer,
#     #                       # unicode, float & complex data types
#     #                       else x.fillna(excluded.update((x+dx, y+dy) for (dx, dy) in deltas)
#     #                                     )
#     #                       )
#     return randPoints

# define function to generate random advert locations
def rand_shuf_loc(str_lst, num):
    lst = adv_loc
    # using list comprehension
    rand_shuf_str = [item for item in lst for i in range(num)]
    # x = random.shuffle(rand_shuf_str)
    return(rand_shuf_str)
    # return(x)

# define function to generate random advert names
def rand_shuf_prod(loc_list, num):
    rand_shuf_str = [item for item in loc_list for i in range(num)]
    random.shuffle(rand_shuf_str)
    return(rand_shuf_str)

# define function to generate random impression and click data
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

def rand_prod_click_timestamp(stime, etime, num):
    prod_clik_tmstmp = []
    # start = "2020-10-01"
    # end = "2020-10-30"
    frmt = '%d-%m-%Y %H:%M:%S'
    # x = 50
    

    for i in range(num):
        # stime = time.mktime(time.strptime(stime, frmt))
        # etime = time.mktime(time.strptime(etime, frmt))
        # td = etime - stime
        # stime = time.mktime(time.strptime(stime, frmt))
        # etime = time.mktime(time.strptime(etime, frmt))

        # ptime = stime + random.random() * (etime - stime)
        # dt = datetime.fromtimestamp(time.mktime(time.localtime(ptime)))
        rtime = int(random.random()*86400)
    
        hours   = int(rtime/3600)
        minutes = int((rtime - hours*3600)/60)
        seconds = rtime - hours*3600 - minutes*60
    
        time_string = '%02d:%02d:%02d' % (hours, minutes, seconds)
        prod_clik_tmstmp.append(time_string)
        time_stmp = [item for item in prod_clik_tmstmp for i in range(num)]
        
    # return {'prod_clik_tmstmp_lst':prod_clik_tmstmp}
    return {'prod_clik_tmstmp_lst':time_stmp}

# Define function that accepts a start date and end date as parameters.
# Ad returns a random series of dates between the given start and end date
# def rand_shuf_date(start_date, end_date, num):
#     start_d = start_date.value//num**9
#     end_d = end_date.value//num**9
#     return (pd.to_datetime(np.random.randint(start_d, end_d)))
# define the main function


def main():
    print('generating data...')
    # print('generating random geographic coordinates...')
    # get the impressions and click data
    impression = rand_clic_impr(num)
    clicks = rand_clic_impr(num)
    product_price = rand_prod_price_discount(num)
    product_discount = rand_prod_price_discount(num)
    prod_clik_tmstmp = rand_prod_click_timestamp("20-01-2018 13:30:00",
                                                 "23-01-2018 04:50:34",num)
    # print("pp: ", product_price)
    # start = rand_shuf_date('2010-10-1', '2010-10-30', 10)
    # end = rand_shuf_date('2010-10-1', '2010-10-30', 10)
    # add all lists to a dictionary
    # lst_dict = {"geog_cord": rand_geog_cord(num),
    #             "ad_loc": rand_shuf_loc(adv_loc, num),
    #             "ad_prod": rand_shuf_prod(adv_prod, num),
    #             "impressions": impression['rand_impr_lst'],
    #             "clicks": clicks['rand_click_lst']}
    lst_dict = {"ad_loc": rand_shuf_loc(adv_loc, num),
                "prod": rand_shuf_prod(adv_prod, num),
                "imprsn": impression['rand_impr_lst'],
                "cliks": clicks['rand_click_lst'],
                "prod_price": product_price['prod_price_lst'],
                "prod_discnt": product_discount['prod_discnt_lst'],
                "prod_clik_stmp": prod_clik_tmstmp['prod_clik_tmstmp_lst']}
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
    res.to_csv("fake_data.csv", sep=",")

# invoke the main function


if __name__ == "__main__":
    main()
