#!/usr/bin/python3
"""Module for Matrix Multiplication"""


def list_of_lists(li):
    """Validating if list of lists"""
    for i in li:
        if not isinstance(i, list):
            return False

    return True


def is_empty(li):
    """Checking for empty matrix or empty list in it"""
    if len(li) == 0:
        return False
    for i in li:
        if len(i) == 0:
            return False
    return True


def int_or_float(li):
    """Validating if all the elements are either float or decimal"""
    for i in li:
        for j in i:
            if not isinstance(j, (int, float)):
                return False

    return True


def is_rectangle(li):
    """Check for Uniformity of Matrix"""
    len_li1 = len(li[0])
    for i in li:
        if len(i) > len_li1 or len(i) < len_li1:
            return False

    return True


def are_multiplicands(m_1, m_2):
    """Checks if multiplicands"""

    if len(m_1[0]) != len(m_2):
        return False

    return True


def solution(m_a, m_b):
    """Finding the result"""
    new_mat = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_mat[i][j] += m_a[i][k] * m_b[k][j]

    return new_mat


def matrix_mul(m_a, m_b):
    """Function for finding product btw two matrices"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not list_of_lists(m_a):
        raise TypeError("m_a must be a list of lists")
    if not list_of_lists(m_b):
        raise TypeError("m_b must be a list of lists")
    if not is_empty(m_a):
        raise ValueError("m_a can't be empty")
    if not is_empty(m_b):
        raise ValueError("m_b can't be empty")
    if not int_or_float(m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not int_or_float(m_b):
        raise TypeError("m_b should contain only integers or floats")
    if not is_rectangle(m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not is_rectangle(m_b):
        raise TypeError("each row of m_b must be of the same size")
    if not are_multiplicands(m_a, m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return solution(m_a, m_b)
