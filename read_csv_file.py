#!/usr/bin/env python3
# Write a Python program to read each row from a given csv file and print dictionary with row values in list


import csv


def read_csv(file_path):
    with open(file_path) as f:
        reader = csv.DictReader(f)
        dictionary = {}
        for i in reader:
            for k, v in i.items():
                if k not in dictionary:
                    dictionary[k] = []
                dictionary[k] += [v]
        return dictionary


        #return data_list
    # for i in reader:
    #    print(','.join(i))


path = input('enter the path to csv file')
print(read_csv(path))
