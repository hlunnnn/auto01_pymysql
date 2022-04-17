"""
演示PyMysql使用的框架代码
"""
#1.整合mysql
import pymysql
#2、创建连接
conn = pymysql.Connect(host="127.0.0.1",port=3306,database="",user="root",password="root")
#3、连接上获取游标对象（cursor）==小毛驴
cursor = conn.cursor()
print(cursor)
print(conn)
#4、核心：发送sql


#5、释放资源
cursor.close()
conn.close()