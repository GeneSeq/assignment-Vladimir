#! /usr/bin/env python


"""
hw 4
"""


from __future__ import  division, print_function
from itertools import izip


# Task 2
def p_distance(seq1, seq2):
    """
    :type seq1: str
    :param seq1:
    :type seq2: str
    :param seq2:
    :return: p-distance between seq1 and sec2
    """
    if len(seq1) != len(seq2):
        raise ValueError("Sequences are not aligned")
    mismatches_without_gaps = sum(char1 != char2 and char1 != "-" and
                                  char2 != "-" for char1, char2 in
                                  izip(seq1, seq2))
    ident_positions = sum(char1 == char2 for char1, char2 in izip(seq1, seq2))
    return mismatches_without_gaps/(mismatches_without_gaps+ident_positions)


# Task 3 (in progress)
def matrix_mul(mx1, mx2):
    """
    :type mx1: list
    :param mx1:
    :type mx2: list
    :param mx2:
    :return: list with result of 2 matrix multiplication
    """
    if ncol_mx1 != nrow_mx2:
        raise ValueError("Matrix is not matched")
    nrow_mx1, ncol_mx1 = len(mx1), len(mx1[0])
    nrow_mx2, ncol_mx2 = len(mx2), len(mx2[0])
    multipl_result = [[None for j in xrange(ncol_mx2)]
                      for i in xrange(nrow_mx1)]
    def get_col(mx, j):
        return [row[j] for row in mx]


