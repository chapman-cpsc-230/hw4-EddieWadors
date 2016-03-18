# -*- coding: utf-8 -*-
"""
File: Heaviside.py

Copyright (c) 2016 Eddie Wadors

License: MIT

Running a test to ensure the heaviside function works correctly.
"""

def H(x):
    if x < 0:
        value = 0
    else:
        value = 1
    return value

def test_H():
    if H(-10) != 0:
        print "error -10 = 0"
    elif H(-10 ** -15) != 0:
        print "error -10**-15 = 0"
    elif H(0) != 1:
        print "error 0 = 1"
    elif H(10 ** 15) != 1:
        print "error 10**15 = 1"
    elif H(10) != 1:
        print "error 10 = 1"
    else:
        print "Correct"

test_H()
