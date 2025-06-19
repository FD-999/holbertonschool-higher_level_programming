#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        for i in row:
            new_matrix += i * i
        return new_matrix
    print() 
