# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 08:39:51 2020

@author: gupta
"""

b = 100

print("b value is =",b, id(b))

b = 200
print("b value is =",b, id(b))

c = 300
print("c value is =",c, id(c))
c += 100
print("c value is =",c, id(c))
c += 100
print("c value is =",c, id(c))
c += 2
print("c value is =",c, id(c))
x = c

print("checking id")
print(x is c)

print("x value is =",x, id(x))
x *= 2
print("x value is =",x, id(x))
print("c value is =",c, id(c))

print("checking id")
print(x is c)


p = 100
p %= 3  # p = p % 3
#print("p value is =",p)

t1 = 100
t2 = 200

print(t1 == t2)
print(t1 != t2)


x1 = "sunil"
x2 = "1"

print(x1 > x2 and x1 == x2)
print(x1 > x2 or x1 == x2)






