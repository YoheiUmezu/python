# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:24:32 2019

@author: adfon07
"""

my_dict = {'school':'definition of school','coding':'definition of coding', 
           'python':'definition of python'}

print(my_dict)

print(my_dict['school'])
#value
#definition of school
#keys are unique

my_dict['pen'] = 'definition of pen'

print(my_dict)
#{'school': 'definition of school', 'coding': 'definition of coding', 'python': 'definition of python', 'pen': 'definition of pen'}

my_dict['school'] = 'key number 2'
print(my_dict)
#{'school': 'key number 2', 'coding': 'definition of coding', 'python': 'definition of python', 'pen': 'definition of pen'}


for key,value in my_dict.items():
    print(key, '  ',value)
    
    #school    key number 2
    #coding    definition of coding
    #python    definition of python
    #pen    definition of pen

my_dict[2] = 'the key is 2'
print(my_dict)
#{'school': 'key number 2', 'coding': 'definition of coding', 'python': 'definition of python', 'pen': 'definition of pen', 2: 'the key is 2'}
print(my_dict[2])
#the key is 2