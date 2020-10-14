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
import numpy as np

# declare global variables
adv_name = ['soft toys', 'kitchenware', 'electronics',
            'mobile phones', 'laptops']
adv_loc = ['cheras', 'universiti', 'sungai besi',
           'ampang', 'kl sentral']
adv_prod = ['baby product', 'kitchenware', 'electronics',
            'mobile phones', 'laptops']
num = 10


# define function to generate random geographic coordinates
def rand_geog_cord(num):
    # Generate a set of all points within 200 of the origin,
    # to be used as offsets later
    # There's probably a more efficient way to do this.
    radius = 200
    rangeX = (0, 2500)
    rangeY = (0, 2500)
    # qty = 100  # or however many points you want
    deltas = set()
    for x in range(-radius, radius+1):
        for y in range(-radius, radius+1):
            if x*x + y*y <= radius*radius:
                deltas.add((x, y))
    randPoints = []
    excluded = set()
    i = 0
    while i < num:
        x = random.randrange(*rangeX)
        y = random.randrange(*rangeY)
        if (x, y) in excluded:
            continue
        randPoints.append((x, y))
        i += 1
        excluded.update((x+dx, y+dy) for (dx, dy) in deltas)
        # print (randPoints)
    # randPoints.apply(lambda x: x.fillna(0)
    #                       if x.dtype.kind in 'biufc'
    #                       # where 'biufc' means boolean, integer,
    #                       # unicode, float & complex data types
    #                       else x.fillna(excluded.update((x+dx, y+dy) for (dx, dy) in deltas)
    #                                     )
    #                       )
    return randPoints

# define function to generate random advert locations
def rand_shuf_loc(str_lst, num):
    lst = adv_loc
    # using list comprehension
    rand_shuf_str = [item for item in lst for i in range(num)]
    random.shuffle(rand_shuf_str)
    return(rand_shuf_str)

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
    # start = rand_shuf_date('2010-10-1', '2010-10-30', 10)
    # end = rand_shuf_date('2010-10-1', '2010-10-30', 10)
    # add all lists to a dictionary
    # lst_dict = {"geog_cord": rand_geog_cord(num),
    #             "ad_loc": rand_shuf_loc(adv_loc, num),
    #             "ad_prod": rand_shuf_prod(adv_prod, num),
    #             "impressions": impression['rand_impr_lst'],
    #             "clicks": clicks['rand_click_lst']}
    
    lst_dict = {"ad_loc": rand_shuf_loc(adv_loc, num),
                "product": rand_shuf_prod(adv_prod, num),
                "impressions": impression['rand_impr_lst'],
                "clicks": clicks['rand_click_lst']}
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
