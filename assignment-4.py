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
        raise ValueError("")
    mismatches_without_gaps = sum(char1 != char2 and char1 != "-" and char2 != "-" for char1, char2 in izip(seq1, seq2))
    ident_positions = sum(char1 == char2 for char1, char2 in zip(seq1, seq2))
    return mismatches_without_gaps/(mismatches_without_gaps+ident_positions)

