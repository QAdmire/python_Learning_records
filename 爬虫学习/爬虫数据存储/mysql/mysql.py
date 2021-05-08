# -*- coding: UTF-8 -*-
import pymysql
import xlrd
'''
结合excel表格快速写入数据
成功实现自动匹配表名和自动生成insert语句

'''
workbook = xlrd.open_workbook('w.xlsx')
#获取excel表名也就是需要插入数据库的数据库的表名
for i in workbook.sheets():
    sheet = workbook.sheet_by_name(i.name)
    #获取excel表的数据
    cells = list()
    for row in range(1, sheet.nrows):
        cell = list()
        for col in range(sheet.ncols):
            if isinstance(sheet.cell_value(row,col),float):
                cell.append(int(sheet.cell_value(row,col)))
            else:
                cell.append(sheet.cell_value(row,col))
        cells.append(cell)

    db = pymysql.connect(
        host="localhost", port=3306, user="root", password="root", database="xsgl1"
    )
    cursor = db.cursor()




    # sql = '''
    # insert into student(sno,sname,ssex,sage,sdept) values(%s,%s,%s,%s,%s,null,null)
    #
    #
    # '''
    for lst in cells:

        t = tuple(lst)
        # 生成sql语句
        sql = 'insert into ' + sheet.name + ' values' + str(t)
        #实现生成插入语句 自动匹配表名 和 通过元组来加入values值
        cursor.execute(sql)
    db.commit()
    db.close()
