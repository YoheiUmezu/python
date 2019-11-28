# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:25:20 2019

@author: adfon07
"""

import xlrd #import

#open workbook
workbook = xlrd.open_workbook('first_file.xlsx')

#get sheet - method -sheet _by_index(index parameter)

worksheet = workbook.sheet_by_index(0)

#find total no of rows - .nrows
'''
print(worksheet.nrows)
'''
rows = worksheet.nrows

#read rows - row_value(row number) -returns a tuple
for row in range(rows):
    first_col,second_col = worksheet.row_values(row)
    print(first_col,' ',second_col)
    
'''
Row Number   0.0
Row Number   1.0
Row Number   2.0
Row Number   3.0
Row Number   4.0
Row Number   5.0
Row Number   6.0
Row Number   7.0
Row Number   8.0
Row Number   9.0
Row Number   10.0
Row Number   11.0
Row Number   12.0
Row Number   13.0
Row Number   14.0
Row Number   15.0
Row Number   16.0
Row Number   17.0
Row Number   18.0
Row Number   19.0
'''
