# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:05:19 2020

@author: gupta

wap to find digits in givennumber. and find if they are in assending order or not.
"""

given_number = 5573297


def find_given_assending(given):
    number_parts = str(given)
    digits = list(number_parts) 
    for pos, digit in enumerate(digits):
        print(pos, digit)
        # if digits[pos] < digits[pos+1]:
            

find_given_assending(given_number)