#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    search = str(search)
    replace = str(replace)
    for i in my_list:
        new_num = int(str(i).replace(search, replace))
        new_list.append(new_num)
    return new_list
