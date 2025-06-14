#!/usr/bin/python3
a = ""
result = ""
b = 0 
for i in "zyxwvutsrqponmlkjihgfedcba":
    a += i
    if b % 2 == 0:
        result += chr(ord(a[b]))
    else:
        result += chr(ord(a[b]) - 32)
    b += 1
print(result)
