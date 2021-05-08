# -*- coding: UTF-8 -*-
import csv

#两种方法
# with open("stock.csv", 'r', encoding='gbk') as fp:
#     reader = csv.reader(fp)
#     for i in reader:
#         print(i)

with open("stock.csv", 'r', encoding='gbk') as fp:
    reader = csv.DictReader(fp)
    for i in reader:
        print(i)