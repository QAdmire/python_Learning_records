import pymysql

db = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="root",database="csdn_crawler")
cursor = db.cursor()

# delete from [表名] 条件
sql = "delete from article where id>3"
cursor.execute(sql)

db.commit()
db.close()