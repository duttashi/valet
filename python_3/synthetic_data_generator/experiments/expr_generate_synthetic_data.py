# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:02:05 2020

@author: Ashish
"""

import time
import random
import string
import pandas as pd
import filepaths


# declare variables
num_of_rows = 100

def main():
    print('generating data...')
    start = time.time()
    
    # declare empty dictionary
    digital_advert_dataset ={}
    print('generating Digital Advert ID numbers...')
    digital_advert_dataset['DA Service ID'] = generate_DA_id_numbers()

    print('generating advert type and location ...')
    (digital_advert_dataset['Type'], digital_advert_dataset['location']) = generate_DA_type_loc()
    
    # write_data_to_disk(digital_advert_dataset, filepaths.digital_advert_dataset)
    # print('dataset written out to: ', filepaths.digital_advert_dataset)


# define custom functions
def generate_DA_id_numbers() -> list:
    """ Generate dummy Health Service ID numbers similar to NHS 10 digit format
    See: https://www.nhs.uk/using-the-nhs/about-the-nhs/what-is-an-nhs-number/
    """
    DA_id_numbers = []
    for _ in range(num_of_rows): 
        DA_id = ''.join(random.choice(string.digits) for _ in range(3)) + '-'   
        DA_id += ''.join(random.choice(string.digits) for _ in range(3)) + '-'   
        DA_id += ''.join(random.choice(string.digits) for _ in range(4))
        DA_id_numbers.append(DA_id)
    return DA_id_numbers

def generate_DA_type_loc() -> (list, list):
    """
    Generates random advert type and location and returns them as list
    """
    # generate 100 random coordinate decimal numbers between 0 and 2
    loc_data = [(random.random()*2.0, random.random()*2.0) for _ in range(100)]
    # loc_data = coords
    # generate 100random advert types
    advert_type = "".join( [random.choice(string.ascii_letters) for i in range(15)] )

    return (loc_data, advert_type)

def write_data_to_disk(dataset: dict, filepath: str):
    """Writing dataset to .csv file
    Keyword arguments:
    dataset -- the dataset to be written to disk
    filepath -- path to write the file out to
    """

    df = pd.DataFrame.from_dict(dataset)
    print(df)
    # df.to_csv(filepath, index=False)


if __name__ == "__main__":
    main()