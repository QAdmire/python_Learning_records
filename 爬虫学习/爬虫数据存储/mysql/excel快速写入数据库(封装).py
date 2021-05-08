# -*- coding: UTF-8 -*-
import pymysql
import xlrd
'''
结合excel表格快速写入数据
成功实现自动匹配表名和自动生成insert语句
利用目前所学实现封装
'''

def link_sql():
    db = pymysql.connect(
        host="localhost", port=3306, user="root", password="root", database="xsgl1"
    )
    return db
def sql(db, cells, i):
    sheet = i
    for lst in cells:

        t = tuple(lst)
        # 生成sql语句
        sql = 'insert into ' + sheet.name + ' values' + str(t)
        #实现生成插入语句 自动匹配表名 和 通过元组来加入values值
        insert_sql(db,sql)
def insert_sql(db,sql):
    cursor = db.cursor()
    cursor.execute(sql)

def save_sql(db):
    db.commit()
    db.close()
    print("插入完成")

def cell(db, i, workbook):
    sheet = workbook.sheet_by_name(i.name)
    # 获取excel表的数据
    cells = list()
    for row in range(1, sheet.nrows):
        cell = list()
        for col in range(sheet.ncols):
            if isinstance(sheet.cell_value(row, col), float):
                cell.append(int(sheet.cell_value(row, col)))
            else:
                cell.append(sheet.cell_value(row, col))
        cells.append(cell)
    sql(db, cells, i)

def main():
    db = link_sql()
    workbook = xlrd.open_workbook('w.xlsx')
    for i in workbook.sheets():
        cell(db, i, workbook)
    save_sql(db)

if __name__ == '__main__':
    main()







#获取excel表名也就是需要插入数据库的数据库的表名

