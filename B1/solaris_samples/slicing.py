# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:22:02 2020

@author: gupta
"""

given = list(range(30))

t = [1,2,3,4,5,6]

print(given[0], " to print 1st")
print(given[5-1], " to print 5st")
print(given[-1], " to print last value")
print(given[-2], " to print 2nd value from last")
print(given[-4], " to print 4th value from last")
print(given[0 : 3], " to print first 3 values")
print(given[4 : 4+5], " to print 4th value till next 5 values")
print(given[1 : -1 : 2], " to print alternative values starting from 1")
print(given[0 : -1 : 2], " to print even position values")
print(given[-1 : -3 : -1], " to print last two values")
print(given[-1 : -11 : -2], " to print alternative from last 10")
print(given)
print(given[-1: 0 : -1])