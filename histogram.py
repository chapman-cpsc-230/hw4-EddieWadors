# -*- coding: utf-8 -*-
"""
File: histogram.py

Copyright (c) 2016 Eddie Wadors

License: MIT

printing a specific # of asterisks for each number of 'n' given
"""
ls = [6, 11, 15, 8]
def bar(n):
    st = ""
    for i in range (n):
        st += "*"
    return st
    
for i in range (len(ls)):
    print bar(ls[i])
print ls
