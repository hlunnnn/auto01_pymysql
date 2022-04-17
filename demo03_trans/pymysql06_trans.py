"""
需求：先往t_book表插入书（三国演义）的信息，然后向t_hero插入该书主角（诸葛亮）的信息，要求：要么都成功，要么都失败
"""
import pymysql

conn = pymysql.Connect(host="localhost",port=3306,database="books",user="root",password="root",charset="utf8") #autocommit=True 自动提交不可以满足当前场景下的事务需求
cursor = conn.cursor()
#核心：使用事务控制两条sql语句执行
#sql1 sql2 运行正常，事务提交，否则，不执行提交（回滚）== try 语句实现分支
try:
    sql1 = "insert into t_book values(5,'三国演义','1999-01-01',1000,800,0)"
    cursor.execute(sql1)
    sql2 = "insert into t_hero values (6,'诸葛亮',1,'足智多谋',0,5)"
    cursor.execute(sql2) #cursor执行sql语句
    #提交事务
    conn.commit()
except Exception as e:
    print(e)
    #执行事务回滚
    conn.rollback()
finally:
    #在finally中关闭资源
    cursor.close()
    conn.close()


