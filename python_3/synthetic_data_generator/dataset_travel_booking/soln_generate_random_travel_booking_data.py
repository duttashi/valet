# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:17:09 2021
Last modified on Feb 24 21:00
Objective: To generate travel booking data
Version: 0.0.1

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
LETTER = string.ascii_lowercase[:12]
ROW_COUNT = 10
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

def get_random_destination(DEST):
    return random.choice(DEST)

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
    lst_orig = re.findall(".{3}", a)
    return lst_orig

def get_airport_dest():
    a = 'USAKULAMRJPNINDRUSPENKULNPLSGR'
    lst_dest = re.findall(".{3}", a)
    return lst_dest
    
def count_passenger_adult():
    return [random.randint(MIN_RANGE, MAX_RANGE) for _ in range(ROW_COUNT)]

def count_passenger_infant():
    return [random.randint(MIN_RANGE, MAX_RANGE) for _ in range(ROW_COUNT)]

def main():
    # clear the console
    clear()
    # declare variables
    start_dt = date(2015, 12, 1)
    end_dt = date(2015, 12, 10)
    travel_date = date(2015, 12, 19)
    email_lst = generate_random_emails(ROW_COUNT,MAX_RANGE)
    lst_airprt_orig = get_airport_orig()
    lst_airprt_dest = get_airport_dest()
    booking_dt = get_booking_dates(start_dt, end_dt)
    
    travel_dt = get_travel_dates(end_dt, travel_date)
    
    lst_adult = count_passenger_adult()
    lst_child = count_passenger_infant()
    df = pd.DataFrame.from_dict({"custmr_email": email_lst,
                       "booking_date": booking_dt,
                       "travel_date": travel_dt,
                       "orig": lst_airprt_orig,
                       "dest": lst_airprt_dest,
                       "guest_adult": lst_adult,
                       "guest_child": lst_child
                       }, orient='index').T
    # repeat the rows in dataframe n times
    df_expanded = df.loc[np.repeat(df.index.values,ROW_COUNT)]
    df_expanded = df_expanded.sample(frac=1).reset_index(drop=True)
    print("Expanded dataframe shape: ", df_expanded.shape)
    print(df_expanded)
    # write dataframe to disc
    df_expanded.to_csv("travel_bookings.csv", sep=',', index=False)
        
if __name__ == "__main__":
    main()


