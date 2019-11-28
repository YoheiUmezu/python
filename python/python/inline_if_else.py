# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:16:48 2019

@author: adfon07
"""

a = 20
if a == 20:
    print('a is 20')
else: 
    print('a is not 20')
#using in-line if else statements
    
print('a is 20' if a == 21 else 'a is not 20') #do somethin if condition else do something
'''
a is 20
a is not 20
'''
b = True if a == 20 else False
print(b)
    
#using in-line if else statements in list comprehensions
    
num = [value for value in range(-5,5)]
print(num)

positive_num = [value for value in num if value > 0]
print(positive_num)
#[1, 2, 3, 4]

