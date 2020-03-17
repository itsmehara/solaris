# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 08:50:26 2020

@author: gupta
"""
#print("test")
x = 1

'''
if conditional statement :
    """
    true block
    """
'''
if x >= 10 :
    print("true block executed")

if x >= 10 :
    print("true block executed")
else:
    print("false block executed")

print("program completed")
y = 33
"""
0 to 20
20 to 30 including 20
30 to infinity including 30
"""

if y >= 0 and y < 20:
    print("first block executed")
elif y >= 20 and y < 30:
    print("second block executed")
elif y >=30 :
    print("third block executed")
else:
    print("given value is less than 0")
    
