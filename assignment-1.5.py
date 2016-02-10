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
        if fn(element, **kwargs):
           true_results.append(element)
    return true_results


# Task 5
# Don't look at this, I just started


def evaluate_string():
    operation_dict = {
        "+": operator.add,
    }
    numbers_iterator = iter(numbers)
    acc = next(numbers_iterator)
    for num, oper in zip(numbers_iterator, operations):
        oper_func = operation_dict.get(oper)
        if not oper_func:
            raise ValueError("Operation {} is not supported".format(oper))
        acc = oper_func(acc, num)
    return acc







def calculate(numbers, operations):
    if len(numbers) != len(operations) + 1:
        raise ValueError("msg")
