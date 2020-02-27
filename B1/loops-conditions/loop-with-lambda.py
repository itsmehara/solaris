# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:07:48 2020

@author: gupta
"""

output = []

x = list(range(20))

y = lambda t : 5*(t**2) + 3*t + 2

for x1 in x:
    #y1 = 5*(x1**2) + 3*x1 + 2
    y1 = y(x1)
    output.append(y1)

print(x)
print( output ) 
