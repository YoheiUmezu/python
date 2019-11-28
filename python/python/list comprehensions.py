# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:49:00 2019

@author: adfon07
"""

import random

print(random.randint(0,100))

#make a list of random values
our_list=[]
for value in range(0,20):
    our_list.append(random.randint(0,100))
    
print(our_list)
#[78, 98, 28, 73, 40, 22, 19, 28, 52, 41, 15, 81, 3, 76, 80, 61, 2, 72, 53, 15]
print(len(our_list))
#20

#making a list using list comprehension

new_list = [value for value in range (0,20)]
#[value whih is being inserted into my list --for loop]
print(new_list)

new_list = [random.randint(0,100) for value in range(0,20)]
print(new_list)
