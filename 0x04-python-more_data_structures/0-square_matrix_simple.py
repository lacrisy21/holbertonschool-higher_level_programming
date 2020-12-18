#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixa = []
    for n in matrix:
        matrixb = list(map(lambda x: x ** 2, n))
        matrixa.append(matrixb)
    return matrixa
