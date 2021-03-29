import pandas as pd
from sys import argv
from os import path


def read_csv(file):
    #convert csv file to pandas dataset
    data = pd.read_csv(file)

    return data


def sort_data(data, column, sort_ascend):
    #sort data set by provided column header
    #Sorting specified as descending
    data.sort_values(by=[column], inplace=True, ascending=sort_ascend)

    return data


def write_csv(data):
    #write dataset to output.csv file
    return data.to_csv("output.csv", index=False)


if __name__ == '__main__':
    #check for correct number of args
    num_args = len(argv)
    if num_args < 2:
        print("Please include column heading to sort by as first argument")
    else:
        in_file = 'input.csv'
        sort_column = argv[1]


        if not path.isfile('input.csv'):
            print('File input.csv is required for input')
        else:
            data = read_csv(in_file)

            if sort_column not in data.head():
                print("Please enter a column heading in the dataset")
            else:

                sorted_data = sort_data(data, sort_column, False)

                if write_csv(sorted_data):
                    print('Error wrtiting file')
