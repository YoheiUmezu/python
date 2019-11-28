# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:39:08 2019

@author: adfon07
"""

person = 'Samy',27,'brown' #tuple

name,age,hair_color = person
print(name)
print(age)
print(hair_color)

print(person)
print(person[2])


#looping

for value in person:
    print(value)
    
#nested person
    
person = 'Summy',('brown','black'),27
print(person[1])

#('brown', 'black')

my_list = [1,2,3]
my_list[0] = 100
print(my_list)
#[100, 2, 3]

person[0] = 'new name'
print(person)

