#使用自定义的pymysql工具类
from demo04_utils.MyUtils import DButil

#获取连接
conn = DButil.get_conn()
#获取游标
cursor = DButil.get_cursor(conn)
#核心：sql语句
sql = "select * from t_book"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)

#释放资源
DButil.close_res(cursor,conn)