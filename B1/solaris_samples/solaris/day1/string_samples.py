# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 08:52:48 2020

@author: gupta

to find number of words in given string.
"""

given_str = "today is good day.     "
given_str2 = "     "

def count_words1():
    str_words = given_str.split()
    print(len(str_words))


def count_words2(str_arg):
    count = 1
    s1 = str_arg.strip()
    slen = len(s1)
    if slen == 0:
        count = 0
    for each_ch in s1:
        if each_ch == " ":
            count = count + 1
    print(count)
    
count_words2(given_str)    
count_words2(given_str2)