# -*- coding: UTF-8 -*-
import xlrd

workbook = xlrd.open_workbook('abc.xls')

#获取所有sheet名字
# print(workbook.sheet_names())

#根据索引获取sheet对象
# sheet = workbook.sheet_by_index(0)
# print(sheet.name)

#根据名字获取sheet对象
# sheet = workbook.sheet_by_name('sheet1')
# print(sheet.name)

#获取所有sheet对象
# sheets = workbook.sheets()
# for i in sheets:
#     print(i.name)

#获取指定sheet对象的行数和列数
# sheet = workbook.sheet_by_index(0)
# print(sheet.nrows,'++++',sheet.ncols)

#/////////////////////////cell//////////////////////////////

sheet = workbook.sheet_by_index(0)
from  xlrd.sheet import Cell
cell = sheet.cell(1,1)
# print(cell.value)

#获取第一行的人的所有成绩
# cells = sheet.row_slice(1,1,4)
# print(cells)

#获取1-5行数学的成绩

# cells = sheet.col_slice(2, 1, 6)
#所有的数学成绩和
cells = sheet.col_values(2,1,sheet.nrows-1)
print(sum(cells))
