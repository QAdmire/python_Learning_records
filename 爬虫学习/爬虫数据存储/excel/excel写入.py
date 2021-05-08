# -*- coding: UTF-8 -*-
import xlwt
import random

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("成绩1")
headers = ['name','语文','数学','English']
for index, header in enumerate(headers):
    sheet.write(0,index,header)
names = ['joab', 'sda', 'pyht', 'dsa']
for index, name in enumerate(names):
    sheet.write(index+1, 0, name)

for row in range(4):
    maths = [random.randint(1, 100) for i in range(4)]
    print(maths)
    print('=' * 50)
    for col in range(4):
        print(row,col)
        sheet.write(row+1, col+1, maths[col])


workbook.save('成绩1.xls')