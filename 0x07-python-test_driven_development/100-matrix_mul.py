#!/usr/bin/python3
"""
Matrix Multipilication Module Doc
"""


def matrix_mul(m_a, m_b):

    """
    multiply two matrix
    Args:
        m_a(list): first matrix
        m_b(list): second matrix
    Raises:
        TypeError: if m_a or m_b are not list type
                   if not each element of list m_a and  m_b not a number
                   if each row of m_a and m_b are equal to each other
        ValueError: if m_a or m_b is empty
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if any(not isinstance(ls, list) for ls in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(ls, list) for ls in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if any(type(i) not in [int, float] for row in m_a for i in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(type(i) not in [int, float] for row in m_b for i in row):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    d = 0
    e = []
    f = []
    for row in range(len(m_a)):
        for col in range(len(m_b[0])):
            for k in range(len(m_a[row])):
                d += m_a[row][k] * m_b[k][col]
            e.append(d)
            d = 0
        f.append(e)
        e = []
    return f
