# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:05:59 2019

@author: adfon07
"""


from xlsxwriter import Workbook #necessary import

# make workbook
workbook = Workbook('first_file.xlsx')


#add work sheet
worksheet = workbook.add_worksheet()

#write function - parameters - (row,column,value)
'''
worksheet.write(0,0,'zero row and zero column')
worksheet.write(0,1,'zero row and one column')

worksheet.write(1,0,'one row and zero column')
worksheet.write(1,1,'one row and one column')
'''
for row in range(20):
    worksheet.write(row,0,'Row Number')
    worksheet.write(row,1,row)

#close workbook
workbook.close()