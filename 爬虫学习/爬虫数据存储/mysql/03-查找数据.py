import pymysql

db = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="root",database="csdn_crawler")
cursor = db.cursor()

sql = "select id,title from article where id>3"
cursor.execute(sql)
# result = cursor.fetchone()
# result = cursor.fetchall()
result = cursor.fetchmany(7)
print(result)

db.close()