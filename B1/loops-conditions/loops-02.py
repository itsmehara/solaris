# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 08:48:26 2020

@author: gupta
"""
output = []

x = list(range(20))

for x1 in x:
    y1 = 5*(x1**2) + 3*x1 + 2
    output.append(y1)

print(x)
print( output ) 
