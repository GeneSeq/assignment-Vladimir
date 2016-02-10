#! usr/bin/env python


"""
homework 1.5 for thersday
"""


from __future__ import division, print_function


# my_filter


def my_filter(fn, elements, **kwargs):
    """
    function as a filter in __builtins__
    """
    true_results = []
    for element in elements:
        result = fn(element, **kwargs)
        if result:
           true_results.append(result)
    return true_results


# Task 5


