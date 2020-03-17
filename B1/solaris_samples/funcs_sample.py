# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 08:48:46 2020

@author: gupta
"""


given_str = "this is a good day , this is a great day"

print(given_str)
a = 2

def func_test(given_str):
    global a
    print(a)
    a = 100
    print(given_str)
    
func_test("hello")
print(a)

def add_all(a, *b):
    tot = 0
    for b1 in b:
        tot = tot+b1 
    tot = tot + a 
    print(tot)
    
l1 = list(range(1,6))
print(l1)    

(x1, x2, x3, x4, x5) = l1
    
add_all(x1, x2, x3, x4, x5)

print(globals())
