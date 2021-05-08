# -*- coding: UTF-8 -*-
import csv
header = ['name', 'age', 'sex']
student = [
    {'name':'张三', 'age':18,'sex': '男'},
    {'name':'张四', 'age':12,'sex': '女'},
    {'name':'张五', 'age':20,'sex': '女'}
]
#两种写入方式
# with open('student.csv', 'w', encoding='gbk', newline= '') as fp:
#     writer = csv.writer(fp)
#     writer.writerow(header)
#     writer.writerows(student)

with open('student.csv', 'w', encoding='gbk', newline= '') as fp:
    writer = csv.DictWriter(fp, header)
    writer.writeheader()
    writer.writerows(student)