import pymysql

# 1. 使用pymysql.connet方法链接数据库
db = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="root",database="csdn_crawler")
# 2. 如果想要操作数据库，还需要获取db上面的cursor对象
cursor = db.cursor()
# 3. 使用cursor.execute来执行sql语句
cursor.execute("select * from article")
result = cursor.fetchone()
print(result)
