#!/usr/bin/env python3
"""
This code opens two csv files and compares their data,

looking for duplicates.
"""

import csv

ENV_FILE = "myenv.env"

def file_opener(filename):
    """
    This reads csv files and returns list of list of row data
    """
    with open(filename, "r") as our_file:
        lines = csv.reader(our_file)
        file_read = [row for row in lines]
    print(file_read)
    return file_read


def main():
    """
    The main function
    """

    file_01 = file_opener("f1.csv")
    file_02 = file_opener("f2.csv")

    dups = []
    no_dups = file_02
    for row in file_01:
        print(row)
        if row in file_02:
            dups.append(row)
        else:
            no_dups.append(row)

    print(f"Duplicates are: {dups}")
    print(f"The Non-Duplicated list is\n\n{no_dups}")
    print(file_01 + file_02)


main()
