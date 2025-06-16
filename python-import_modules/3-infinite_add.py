#!/usr/bin/python3
import sys
result = 0
if __name__ == "__main__":
    argv = sys.argv[1:]
    count = len(argv)
    if count == 0:
        print("0")
    else:
        for i in range(count):
            result += int(argv[i])
        print(result)
