# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:17:09 2021
Last modified on Feb 27 2021 at 21:00
Objective: To generate travel booking data
Version: 0.0.2

Note:
1. Change the value for ROW_COUNT variable to generate n number of rows
2. This script is the working version of script `expr_generate_random_travel_booking_data` 
@author: Ashish
"""

# declare Global variables and import required libraries
import random, string, re, os
import numpy as np
import pandas as pd
from datetime import timedelta, date

# declare some global variables
DOMAIN = ["hotmail.com", "gmail.com", "aol.com",
          "mail.com", "mail.kz", "yahoo.com"]
DEST = ["KUL", "IND", "AUS", "CHN", "USA", "UK"]
ORIG = ["KUL", "IND", "AUS", "CHN", "USA", "UK"]
TRIPTYPE = ["OneWay","RoundTrip","CircleTrip"]
FLIGHT_DAY = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
BUY_INSURANCE = ['yes','no']
LETTER = string.ascii_lowercase[:12]
ROW_COUNT = 300
MIN_RANGE = 0
MAX_RANGE = 9

# clear the interpreter console screen
def clear():
    print("\033[H\033[J")

def get_random_domain(DOMAIN):
    return random.choice(DOMAIN)

def get_random_name(letters, MAX_RANGE):
    return ''.join(random.choice(letters) for i in range(MAX_RANGE))

def generate_random_emails(ROW_COUNT, MAX_RANGE):
    return [get_random_name(LETTER, MAX_RANGE) + '@' + get_random_domain(DOMAIN) for i in range(ROW_COUNT)]

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
    return [random.randint(MIN_RANGE, MAX_RANGE) for _ in range(ROW_COUNT)]

def count_passenger_infant():
    return [random.randint(MIN_RANGE, MAX_RANGE) for _ in range(ROW_COUNT)]

def get_random_flightday():
    random.shuffle(FLIGHT_DAY)
    return FLIGHT_DAY

def get_random_insurance():
    random.shuffle(BUY_INSURANCE)
    return BUY_INSURANCE

def main():
    # clear the console
    clear()
    # declare variables
    start_dt = date(2015, 12, 1)
    end_dt = date(2015, 12, 10)
    travel_date = date(2015, 12, 19)
    email_lst = generate_random_emails(ROW_COUNT,MAX_RANGE)
    airprt_orig = get_airport_orig()
    airprt_dest = get_airport_dest()
    trip = get_random_triptype()
    booking_dt = get_booking_dates(start_dt, end_dt)
    travel_dt = get_travel_dates(end_dt, travel_date)
    count_adult = count_passenger_adult()
    count_child = count_passenger_infant()
    insurance = get_random_insurance()
    flightday = get_random_flightday()
    df = pd.DataFrame.from_dict({"email": email_lst,
                       "booking_date": booking_dt,
                       "travel_date": travel_dt,
                       "orig": airprt_orig,
                       "dest": airprt_dest,
                       "guest_adult": count_adult,
                       "guest_child": count_child,
                       "trip_type":trip,
                       "flight_day": flightday,
                       "insurance": insurance
                       }, orient='index').T
    # repeat the rows in dataframe n times
    df_expanded = df.loc[np.repeat(df.index.values,ROW_COUNT)]
    df_expanded = df_expanded.sample(frac=1).reset_index(drop=True)
    print("### Data Generated ###\n")
    print("Expanded dataframe shape: ", df_expanded.shape)
    
    # if both origin and destination cols are blank then drop the row
    # nake a copy
    df_clean = df_expanded
    # df_new = df_new[(df_new.orig!="") & (df_new.dest!="")]
    df_clean = df_clean[df_clean.orig.notnull()]
    df_clean = df_clean[df_clean.dest.notnull()]
    df_clean = df_clean[df_clean.trip_type.notnull()]
    
    print("Revised dataframe shape: ", df_clean.shape)
    # write generated data to disc
    df_clean.to_csv("../data/travel_booking_rev.csv", sep=',', index=False)
    
if __name__ == "__main__":
    main()


