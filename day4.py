import pandas as pd
import numpy as np


def string_to_list(string):
    str_list = string.split(" ")  # Split the string into a list, seperator is " "
    while '' in str_list:
        str_list.remove('')  # Remove the empty items from the list
    return str_list


def find_item_indices(list, item):  # returns the indices of item in list
    if item in list:
        return [i for i, x in enumerate(list) if x == item]
    else:
        return False


def check_more_than_one_item(list): # Find if the list contains more than one item
    if len(list) > 0:
        return True
    else:
        return False


def check_duplicates(list):
    dup = 0
    for index in range(len(list)):
        if list.count(list[index]) > 1:
            dup += 1
    if dup > 0:
        return True
    else:
        return False


csvfile = pd.read_csv("day4_input.csv", header=None)
m = np.array(csvfile)

counter = 0
for row in m:
    string = row[0]
    str_list = string_to_list(string)
    more_than_one_item = check_more_than_one_item(str_list)

    has_duplicate = check_duplicates(str_list)

    if more_than_one_item and not has_duplicate:
        counter += 1

print("The numbers of valid passphrase is: " + str(counter))
