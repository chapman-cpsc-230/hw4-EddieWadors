# -*- coding: utf-8 -*-
"""
File: smoothed_heaviside.py

Copyright (c) 2016 Eddie Wadors

License: MIT

Testing a function by defining a test for the function
"""
from math import pi, sin

def H_eps(x, eps = 0.01):
    if x < -eps:
        result = 0
    elif x <= eps:
        x_o_eps = (x/eps)
        result = 0.5*(1+(x_o_eps)+(sin(pi*(x_o_eps)))/pi)
    else:
        result = 1
    return result

def test_H():
    if H_eps(-0.02) != 0:
        print "error #1"
    elif H_eps(-0.01) != 0.5*(1+(1/0.01)+(sin(pi*(-1/0.01)))/pi):
        print "error #2"
    elif H_eps(0) != 0.5*(1+(0/0.01)+(sin(pi*0/0.01))/pi):
        print "error #3"
    elif H_eps(0.01) != 0.5*(1+(1/0.01)+(sin(pi*1/0.01))/pi):
        print "error #4"
    elif H_eps(0.02) != 1:
        print "error #5"
    else:
        print "Correct"
test_H()
