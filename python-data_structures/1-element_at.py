#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    else:
        for i in (my_list):
            num = my_list[idx]
            print(f"Element at index {} is {}".format(idx, num))
