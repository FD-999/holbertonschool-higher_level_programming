#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = []
    if len(my_list) == 0:
        return None
    else:
        my_list.sort()
        max_value.extend(my_list)
        print("Max: {}".format(max_value[-1])
