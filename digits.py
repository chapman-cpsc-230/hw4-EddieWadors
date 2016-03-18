# -*- coding: utf-8 -*-
"""
File: digits.py

Copyright (c) 2016 Eddie Wadors

License: MIT

function that calculates the number of digits of a given number by returning the length of the string given using the len function of python.
"""
def digits(n):
    return len(str(n))
print digits(-1000000)
