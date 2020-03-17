# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 08:47:40 2020

@author: gupta
"""

x = "abc"
print("x is of type = ",type(x))
print(dir(str))

x1 = "given string, is something, good string."
print("--"*10)
print( x1.split() )
print( x1.split("i") )
print( x1.split(",") )

print( x1.rsplit() )
print( x1.rsplit("i") )
print(help(x1.rsplit))

print(help(x1.split))

