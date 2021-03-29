import pandas as pd
from sys import argv


def read_csv(file):
    data = pd.read_csv(file)

    return data


def sort_data(data, column, sort_ascend):
    data.sort_values(by=[column], inplace=sort_ascend)

    return data


def write_csv(data):
    data.to_csv("output.csv", index=False)


if __name__ == '__main__':
    num_args = len(argv)
    in_file = argv[1]
    sort_column = argv[2]

    data = read_csv(in_file)

    sorted_data = sort_data(data, sort_column, True)

    write_csv(sorted_data)
