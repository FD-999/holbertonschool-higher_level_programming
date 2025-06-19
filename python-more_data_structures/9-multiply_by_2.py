#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = {}
    for key in a_dictionary:
        new_list[key] = a_dictionary[key] * 2
    sorted_dict = dict(sorted(new_list.items(), key=lambda x: x[1]))
    return sorted_dict
