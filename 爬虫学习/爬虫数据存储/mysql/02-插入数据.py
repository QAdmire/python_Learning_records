import pymysql

db = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="root",database="csdn_crawler")
cursor = db.cursor()
# sql = "insert into article(id,title,content) values(null,'222','333')"
# cursor.execute(sql)

title = '444'
content = '555'
sql = "insert into article(id,title,content) values(null,%s,%s)"
cursor.execute(sql,(title,content))

db.commit()
db.close()