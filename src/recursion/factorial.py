""" Factorial Solution using Recursion """


def factorial(factor):
    if factor in [0, 1]:
        return 1
    else:
        return factor * factorial(factor - 1)
