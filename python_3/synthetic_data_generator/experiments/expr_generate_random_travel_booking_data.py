# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:17:09 2021
Last modified on Feb 22 21:00
Objective: generate travel booking data
@author: Ashish

"""
import random, string, re
import numpy as np
from datetime import timedelta, date

# declare some global variables
domains = [ "hotmail.com", "gmail.com", "aol.com", 
           "mail.com" , "mail.kz", "yahoo.com"]
dest = ["KUL","IND","AUS","CHN","USA","UK"]
orig = ["KUL","IND","AUS","CHN","USA","UK"]
letters = string.ascii_lowercase[:12]
ROW_COUNT = 10 # denotes number of rows 
RANGE_MIN = 1
RANGE_MAX = 11

def get_random_domain(domains):
    return random.choice(domains)

def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_emails(nb, length):
    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]

def get_random_destination(dest):
    return random.choice(dest)

# generate travel booking dates
def get_booking_dates(date1, date2):
    list_of_dates = []
    for n in range(int ((date2 - date1).days)+1):
        list_of_dates.append(date1 + timedelta(n))
    return list_of_dates

# generate travel date

def get_travel_dates(date1, date2):
    list_of_dates = []
    for n in range(int ((date2 - date1).days)+1):
        list_of_dates.append(date1 + timedelta(n))
    return list_of_dates

# generate random origin and destination locations
def get_airport_orig():
    a = 'KULAMRJPNINDRUSPENKULNPLSGRUSA'
    # lst = [str[i:i+3] for i in range(0, len(a), 3)]
    lst_orig = re.findall(".{3}", a)
    # print(lst)
    # improve this function by generating 3 character words N number of times
    # lst_orig = ['KUL','AMR','BGLR','NDL','PEN','JPN','IND','NPL','AUS','UK']
    return lst_orig
    # return random.sample(lst_orig,1)

def get_airport_dest():
    # Objective: split the given string into 3 character words and return
    a = 'USAKULAMRJPNINDRUSPENKULNPLSGR'
    # lst_dest = ['UK','KUL','AMR','BGLR','NDL','PEN','JPN','IND','NPL','AUS']
    lst_dest = re.findall(".{3}", a)
    return lst_dest
    # return random.sample(lst_dest,1)

def count_passenger_adult():
    # if (RANGE_MAX <= ROW_COUNT):
    return random.sample(range(RANGE_MIN ,RANGE_MAX), ROW_COUNT)
    # else:
    #     # print("### ERROR, ENSURE COUNT OF ROWS IS GREATER THAN MAX RANGE")
    #     return random.sample(range(RANGE_MIN ,RANGE_MAX), ROW_COUNT)

def count_passenger_infant():
    
    return random.sample(range(RANGE_MIN ,RANGE_MAX), ROW_COUNT)
    # return random.sample(range(1,20), ROW_COUNT)
    
def passenger_count():
    
    return random.sample(range(RANGE_MIN ,RANGE_MAX), ROW_COUNT)
    # return a random count of passengers in a given range
    # return random.sample(range(1,20), ROW_COUNT)


def main():
    start_dt = date(2015, 12, 1)
    end_dt = date(2015, 12, 10)
    travel_date = date(2015, 12, 19)
    # 7 refers to the number of chars in username part of the email id
    # count_of_rows refers to the number of email address required
    # print(generate_random_emails(10, 7))
    # print(get_random_destination(dest))
    email_lst = generate_random_emails(ROW_COUNT,7)
    lst_orig = get_airport_orig()
    lst_dest = get_airport_dest()
    
    # print(lst_orig)
    # print('booking date')
    # for dt in get_booking_dates(start_dt, end_dt):
    #     # print(dt.strftime("%Y-%m-%d"))
    #     print(dt)
    # # print("travel date")
    # for dt in get_travel_dates(end_dt, travel_date):
    #     print(dt)
    
    booking_dt = get_booking_dates(start_dt, end_dt)
    travel_dt = get_travel_dates(end_dt, travel_date)
    # for dt in travel_dt:
    #     print(dt)
    # print(passenger_count())
    # lst_guest = passenger_count()
    lst_adult = count_passenger_adult()
    lst_child = count_passenger_infant()
    
    # add all lists into a dataframe
    import pandas as pd
    df = pd.DataFrame({"custmr_email": email_lst,
                       "booking_date": booking_dt,
                       "travel_date": travel_dt,
                       "orig": lst_orig,
                       "dest": lst_dest,
                       "guest_adult": lst_adult,
                       "guest_child": lst_child
                       }
                      )
    # print(df)
    # repeat the rows in dataframe n times
    # df_expanded = df.loc[np.repeat(df.index.values,df.guest_num)]
    # print(df_expanded)
    # num_of_rows = 3
    df_expanded = pd.concat([df]*ROW_COUNT, ignore_index=True)
    # Now randomly shuffle the rows
    # reference: https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows
    df_expanded = df_expanded.sample(frac=1).reset_index(drop=True)
    print(df_expanded)
        
if __name__ == "__main__":
    main()

