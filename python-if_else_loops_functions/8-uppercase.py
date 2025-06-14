#!/usr/bin/python3
result = ""
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            result += chr(ord(i) - 32)
        else:
            result += i
    print("{}".format(result))
