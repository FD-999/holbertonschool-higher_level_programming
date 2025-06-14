#!/usr/bin/python3
result = ""
def uppercase(str):
    for i in str:
        if ord(c) >= 97 and ord(c) <= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
