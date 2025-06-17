#!/usr/bin/python3
def multiple_returns(sentence):
    s = 0
    for i in sentence:
        s += 1
        if s == 0:
            print(f"Length: {s} - First character: None")
    print(f"Length: {s} - First character: {sentence[0]}")
