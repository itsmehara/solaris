# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:33:49 2020

@author: gupta
"""

def test():
    a = 3.73
    print(type(a))
    
    given = ['Beef', 'Cheeeeeese', 'Cheeeese', 'Cheese',
             'Cheeze', 'Chick', 'Chicken', 'Chicken65', 
             'Eggs', 'Fish', 'Freeze', 'Goat', 'Hen', 
             'Lamb', 'Mutt', 'Mutton', 'Muttttton', 
             'Protein Shake', 'Protein Suppliments', 
             'Pulses', 'Soy', 'Soya', 'hicken']

    actual = ['Beef', 'Cheese', 'Cheese', 'Cheese', 
              'Cheese', 'Chicken', 'Chicken', 'Chicken',
              'Eggs', 'Fish', 'Fish', 'Mutton', 'Chicken',
              'Mutton', 'Mutton', 'Mutton', 'Mutton',
              'Protein Shake', 'Protein Suppliments',
              'Pulses', 'Soya', 'Soya', 'Chicken']

    
    mappings = dict(zip(given,actual))
    

test()