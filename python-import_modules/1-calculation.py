#!/usr/bin/python3
from calculator_1 import add
def add(a, b):
    if __name__ == "__main__":
        a = 10
        b = 5
        result = add(a, b)
        print("{} + {} = {}".format(a, b, result))
