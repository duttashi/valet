# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:17:09 2021
Last modified on Feb 24 21:00
Objective: generate travel booking data
@author: Ashish

"""
import random, string, re, os
import numpy as np
import pandas as pd
from datetime import timedelta, date

# declare some global variables
DOMAIN = [ "hotmail.com", "gmail.com", "aol.com", 
           "mail.com" , "mail.kz", "yahoo.com"]
DEST = ["KUL","IND","AUS","CHN","USA","UK"]
ORIG = ["KUL","IND","AUS","CHN","USA","UK"]
TRIPTYPE = ["OneWay","RoundTrip","CircleTrip"]

LETTER = string.ascii_lowercase[:12]
ROW_COUNT = 10 # denotes number of rows 
MIN_RANGE = 0
MAX_RANGE = 9

# clear the interpreter console screen
def clear():
    # got this solution from SO: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    print("\033[H\033[J")
    

def get_random_domain(DOMAIN):
    return random.choice(DOMAIN)

def get_random_name(letters, MAX_RANGE):
    return ''.join(random.choice(letters) for i in range(MAX_RANGE))

def generate_random_emails(ROW_COUNT, MAX_RANGE):
    return [get_random_name(LETTER, MAX_RANGE) + '@' + get_random_domain(DOMAIN) for i in range(ROW_COUNT)]

# generate booking dates
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
    
    # shuffle the list
    random.shuffle(ORIG)
    return ORIG

def get_airport_dest():
    # shuffle the list
    random.shuffle(DEST)
    return DEST

def get_random_triptype():
    # shuffle the list
    random.shuffle(TRIPTYPE)
    return TRIPTYPE

def count_passenger_adult():
    # if (RANGE_MAX <= ROW_COUNT):
    # result = list(range(RANGE_MIN, RANGE_MAX))
    # print("\n in count passenger adult function: ", len(result))
    
    # return random.randint(RANGE_MIN, RANGE_MAX) for _ in range(ROW_COUNT)
    # return random.sample(result, ROW_COUNT)
    # return random.sample(range(RANGE_MIN ,RANGE_MAX), ROW_COUNT)
    # else:
    #     # print("### ERROR, ENSURE COUNT OF ROWS IS GREATER THAN MAX RANGE")
    #     return random.sample(range(RANGE_MIN ,RANGE_MAX), ROW_COUNT)
    # elem = random.shuffle(list(random.shuffle(RANGE_MIN, RANGE_MAX)))
    # print(elem)
    
    
    return [random.randint(MIN_RANGE, MAX_RANGE) for _ in range(ROW_COUNT)]

def count_passenger_infant():
    
    return [random.randint(MIN_RANGE, MAX_RANGE) for _ in range(ROW_COUNT)]
    
    # result = list(range(RANGE_MIN, RANGE_MAX))
    # return random.shuffle(result)
    
    # return random.sample(range(RANGE_MIN ,RANGE_MAX), ROW_COUNT)
    # return random.sample(range(1,20), ROW_COUNT)
    
# def passenger_count():
    
#     return random.sample(range(RANGE_MIN ,RANGE_MAX), ROW_COUNT)
#     # return a random count of passengers in a given range
#     # return random.sample(range(1,20), ROW_COUNT)


def main():
    
    # clear the console
    clear()
    
    # declare variables
    start_dt = date(2015, 12, 1)
    end_dt = date(2015, 12, 10)
    travel_date = date(2015, 12, 19)
    # 7 refers to the number of chars in username part of the email id
    # count_of_rows refers to the number of email address required
    # print(generate_random_emails(10, 7))
    # print(get_random_destination(dest))
    email_lst = generate_random_emails(ROW_COUNT,MAX_RANGE)
    print("Row count: ", ROW_COUNT, "max range: ", MAX_RANGE)
    print("email list len: ", len(email_lst))
    lst_airprt_orig = get_airport_orig()
    print("airport orig list len: ", len(lst_airprt_orig))
    lst_airprt_dest = get_airport_dest()
    print("airport dest list len: ", len(lst_airprt_dest))
    
    # print(lst_orig)
    # print('booking date')
    # for dt in get_booking_dates(start_dt, end_dt):
    #     # print(dt.strftime("%Y-%m-%d"))
    #     print(dt)
    # # print("travel date")
    # for dt in get_travel_dates(end_dt, travel_date):
    #     print(dt)
    
    booking_dt = get_booking_dates(start_dt, end_dt)
    print("book date list len: ", len(booking_dt))
    travel_dt = get_travel_dates(end_dt, travel_date)
    print("travel date list len: ", len(travel_dt))
    # for dt in travel_dt:
    #     print(dt)
    # print(passenger_count())
    # lst_guest = passenger_count()
    lst_adult = count_passenger_adult()
    print("adult passngr count list len: ", len(lst_adult))
    lst_child = count_passenger_infant()
    print("child passngr count list len: ", len(lst_child))
    print("Max range:", MAX_RANGE)
    lst_triptype = get_random_triptype()
    print("Trip type: ",lst_triptype)
    # add all lists into a dataframe
    # Note: using from_dict(), orient='index').T arranges columns with unequal length together
    df = pd.DataFrame.from_dict({"custmr_email": email_lst,
                       "booking_date": booking_dt,
                       "travel_date": travel_dt,
                       "orig": lst_airprt_orig,
                       "dest": lst_airprt_dest,
                       "guest_adult": lst_adult,
                       "guest_child": lst_child,
                       "trip_type":lst_triptype,
                       }, orient='index').T
    # df.explode('orig').reset_index(drop=True)
    # df.explode('dest').reset_index(drop=True)

    # print(df)
    print("orig dataframe shape: ",df.shape)
    # print()
    # repeat the rows in dataframe n times
    df_expanded = df.loc[np.repeat(df.index.values,ROW_COUNT)]
    # print(df_expanded)
    # # num_of_rows = 3
    # df_expanded = pd.concat([df]*ROW_COUNT, ignore_index=True)
    # Now randomly shuffle the rows
    # reference: https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows
    df_expanded = df_expanded.sample(frac=1).reset_index(drop=True)
    print("Expanded dataframe shape: ", df_expanded.shape)
    print(df_expanded)
    # write generated data to disc
    df_expanded.to_csv("../data/booking_data.csv", sep=',', index=False)
        
if __name__ == "__main__":
    main()

