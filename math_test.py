"""Factorial"""
import math


def wrapper(arg1):
    """CalculateFactorial"""
    if not(isinstance(arg1, (int))):
        msg = "must be int"
        raise TypeError(msg)
    return math.factorial(int(arg1))


assert(wrapper(3)) == 6
