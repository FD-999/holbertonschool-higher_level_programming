#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        new_num = int(str(i).replace("2", "89"))
        new_list.append(new_num)
    return new_list
