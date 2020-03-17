# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 08:21:41 2020

@author: gupta
"""
#11th 12th

import hack03 as xyz

#def find_even(given_items):
def find_even(all_given_items):    
    pass
    output = []
    x = 100
    for ev in all_given_items:
        if ev % 2 == 0:
            #print(ev)
            output.append(ev)
        t1 = 23    
    return output, x
t = 231

def main():
    all_given_items = 2,3,4,26,22,36
    #print(type(given_items))
    op = find_even(all_given_items)
    print(op)
    op = find_even(    (4,1,2,4,5,8,66,85,33,53)   )
    print(op)
    print(__name__)

p = 4923

if __name__ == "__main__":
    main()
    print(xyz.__name__)
    