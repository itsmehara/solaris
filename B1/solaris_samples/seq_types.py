# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:09:39 2020

@author: gupta
"""

s1 = ("btech", "Sunil", 12232, "sunil@gmail.com", "ECE")
s2 = ["btech", "charan", 13411, "charan@gmail.com", "ECE"]
print(s1)
print(s1[0])
print(s1[3])
s1_length = len(s1)
print(s1[s1_length - 1]) 
print(s1[4]) 

print(s1[-1])
print(s1[-2])
print("--- Using For Loop with tuple---")
print("-"*10)
print(dir(s1))

print("-"*10)
print(dir(s2))
print("-"*10)
for each_val in s1:
    print(each_val)
    #print("-"*10)

print("--- Using For Loop with List---")

s2.append("SIIET College")

print(s2)

for each_val in s2:
    print(each_val)
    #print("-"*10)











