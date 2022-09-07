#!/usr/bin/python3
"""
Module That Operate on Matxrix
"""


def matrix_divided(matrix, div):

    """
    Divide matrxi elements by div elements
    Args:
        matrix(list): first matrix
        div(list): second matrix
    """
    if any(type(i) not in [int, float] for row in matrix for i in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if matrix == []:
        raise TypeError("matrix must be a matrix\
            (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    size = 0
    if matrix and matrix[0]:
        size = len(matrix[0])
        if any(len(row) != size for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i/div, 2) for i in row] for row in matrix]
