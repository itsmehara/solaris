# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 08:54:01 2020

@author: gupta
"""

"""
*****
*****
*****
*****
*****
"""
for j in range(5):
    for i in range(5):
        print("*", end="")
    print()
#---------------------
"""
*****
****
***
**
*
"""    
for j in range(6):
    for i in range(j,6):
        print("*", end="")
    print()

#---------------------
"""
*
**
***
****
*****
"""    
for i in range(1,6):
    print("*" * i)
