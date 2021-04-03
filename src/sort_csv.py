#!/usr/bin/env python
import pandas as pd
from sys import argv
from os import path


def read_csv(file):
    #convert csv file to pandas dataset
    data = pd.read_csv(file)
    print('\nRead CSV:')
    print(data)
    return data


def sort_data(data, columns, sort_ascend):
    #sort data set by provided list of column headers
    #Sorting specified as descending

    data.sort_values(by=columns, inplace=True, ascending=sort_ascend)

    return data


def write_csv(data):
    #write dataset to output.csv file
    print('\nWrote CSV:')
    print(data)
    return data.to_csv("output.csv", index=False)


if __name__ == '__main__':
    #check for correct number of args
    num_args = len(argv)
    if num_args < 2:
        sort_columns = input("Please enter heading column to sort: ")
    else:
        sort_columns = argv[1]

    sort_columns_list = sort_columns.strip().split(',')
    
    IN_FILE = 'input.csv'
    
    error_msg = ""

    if not path.isfile('input.csv'):
        print('File input.csv is required for input')
    else:
        data = read_csv(IN_FILE)

        for col in sort_columns_list:

            if col not in data.head():
                error_msg = "Please enter a column heading in the dataset"
                break
        
        if len(error_msg) > 0:
            print(error_msg)
        else:

            sorted_data = sort_data(data, sort_columns_list, False)

            if write_csv(sorted_data):
                print('Error wrtiting file')
