"""
演示PyMysql使用的框架代码
"""
#1.整合mysql
import pymysql
#2、创建连接
conn = pymysql.Connect(host="localhost",port=3306,database="books",user="root",password="root",charset="utf8")
#3、连接上获取游标对象（cursor）==小毛驴
cursor = conn.cursor()
#4、核心：发送sql,以及结果处理
sql = "select * from t_book"
cursor.execute(sql) #cursor执行sql语句
#解析结果（游标响应回来数据）
#1）、获取响应的结果行数
print("响应结果行数：",cursor.rowcount)
#2）、获取单条数据
# row1 = cursor.fetchone();print(row1)
# row2 = cursor.fetchone();print(row2)
# row3 = cursor.fetchone();print(row3)
#3）、获取所有数数
rows = cursor.fetchall();print("所有数据：",rows)
for row in rows:
    print("ID:",row[0])
    print("书名:",row[1])
    print("发行日期:",row[2])
    print("阅读量:",row[3])
    print("评论量:",row[4])

#5、释放资源
cursor.close()
conn.close()

#补充：如果涉及到中文，为了避免乱码，最好将charset设置为utf8