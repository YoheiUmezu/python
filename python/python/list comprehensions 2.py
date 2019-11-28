# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:51:44 2019

@author: adfon07
"""

carts = [['toothpaste','shoes','brand'],['pencils','eracers','notebook'],['meat','fruit','vegitables']]
person1 = ['toothpaste','shoes','bread']
person2 = ['pencils','eracers','notebook']
person3 = ['meat','fruit','vegitables']

carts = [person1,person2,person3]

print(carts)

#[['toothpaste', 'shoes', 'bread'], ['pencils', 'eracers', 'notebook'], ['meat', 'fruit', 'vegitables']]

for value in carts:
    print(value)
    
    
print(carts[2][2])
#person3 value3
#vegitables

'''
0,0 0,1 0,2
1,0 1,1 1,2
2,0 2,1 2,2
'''

print(carts[0][0]) #row column



task_list = []

for value in range(0,25,5):
    print(value)

'''
0
5
10
15
20
'''

for row in range(0,25,5):
    inner_list = []
    for column in range(row,row+5):
        inner_list.append(column)
        task_list.append(inner_list)
for row in task_list:
    print(row)
    
'''
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[10, 11, 12, 13, 14]
[10, 11, 12, 13, 14]
[10, 11, 12, 13, 14]
[10, 11, 12, 13, 14]
[10, 11, 12, 13, 14]
[15, 16, 17, 18, 19]
[15, 16, 17, 18, 19]
[15, 16, 17, 18, 19]
[15, 16, 17, 18, 19]
[15, 16, 17, 18, 19]
[20, 21, 22, 23, 24]
[20, 21, 22, 23, 24]
[20, 21, 22, 23, 24]
[20, 21, 22, 23, 24]
[20, 21, 22, 23, 24]
'''

#Use list comprehension to make the same 2-d list

new_list = [[column for column in range(row,row+5)]for row in range(0,25,5)]  #[value which is to be added -- loop]
for row in new_list:
    print(row)

'''
0 1 2 3 4
5 6 7 8 9
10 11 12 13
14 15 16 17
18 19 20 21
'''



