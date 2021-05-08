import pymysql

db = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="root",database="csdn_crawler",charset='utf8')
cursor = db.cursor()

# update [表名] 更新操作 条件
sql = "update article set title='钢铁是怎样练成的' where id=3"
cursor.execute(sql)

db.commit()
db.close()