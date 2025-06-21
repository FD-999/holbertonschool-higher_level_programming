#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    length = list_length
    for i in range(length):
        try:
            div =  my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            div = 0
        finally:
            result.append(div)
    return result
