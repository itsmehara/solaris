# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:16:38 2020

@author: gupta

count number of times each word occurred in given string.
find count of each digits in given number.
find specific digit found in given number.
"""

# this program is incomplete. need to explain further.

given_str = "this is a good day , this is a great day"


def count_words(given):
    words = given.split()
    for word in words:
        print(word)

    #print(*words)
    #print(words[0], words[1], words[2], words[3], words[4])
    
count_words(given_str) #, 1,2,3,4,5, "dfsd", "the", 500)


    