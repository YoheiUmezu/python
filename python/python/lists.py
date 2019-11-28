# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:11:48 2019

@author: adfon07
"""

my_list = [4,3,2,1]
print(my_list[3])


print(my_list[0:3])
print(my_list[0:2]) #2elements

my_list.append(5)
print(my_list)

print(my_list.pop(0))
print(my_list) #remove 4

my_list.remove(3)
print(my_list)

my_list.insert(1,100)
print(my_list)

my_list = [4,3,2,1,1,1,1]

print(my_list.index(1))

print(my_list)
#[4, 3, 2, 1, 1, 1, 1]
my_list.sort()
print(my_list)
#[1, 1, 1, 1, 2, 3, 4]



