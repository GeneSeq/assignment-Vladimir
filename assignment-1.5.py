#! usr/bin/env python


"""
homework 1.5 for thersday
"""


from __future__ import division, print_function


# my_filter
# May be quite primitive, but I can do nothing more interesting


def my_filter(fn, elements, **kwargs):
    all_results = []
    for element in elements:
        all_results.append(fn(element, kwargs))
    true_results = []
    for result in all_results:
        if bool(result) == True:
            true_results.append(result)
    return true_results


# Task 5


