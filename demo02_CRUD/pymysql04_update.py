"""
修改t_book数据
"""
#1.整合mysql
import pymysql
#2、创建连接
conn = pymysql.Connect(host="localhost",port=3306,database="books",user="root",password="root",charset="utf8")
#3、连接上获取游标对象（cursor）==小毛驴
cursor = conn.cursor()
#4、核心：发送sql,以及结果处理
sql = "update t_book set title='后西游记' WHERE id=4;"
cursor.execute(sql) #cursor执行sql语句
#事务提交
conn.commit()

#解析结果（游标响应回来数据）
#1）、获取响应的结果行数
print("新增行数：",cursor.rowcount)

#5、释放资源
cursor.close()
conn.close()

#补充：增删改默认sql不提交，数据不写入数据，需要提交事务
#提交方式1：conn.commit() ==手动提交
#提交方式2：pymysql.Connect(..... autocommit=True)，该值默认是false