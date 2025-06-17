#!/usr/bin/python3
def no_c(my_string):
    for i in (my_string):
        if i != "c" and i != "C":
            return my_string
        else:
            my_string.remove("c")
            my_string.remove("C")
        return my_string
