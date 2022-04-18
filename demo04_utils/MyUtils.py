"""
需求：封装pymysql工具类
"""
import pymysql

class DButil:
    #封装获取连接的函数
    #返回值 connection
    #参数不设置，直接写死，因为后期从配置文件读取
    @classmethod
    def get_conn(cls):
        conn = pymysql.Connect(host="localhost",port=3306,database="books",
                               user="root",password="root",charset="utf8")
        return conn

    #封装获取游标对象的函数
    #参数对象：连接对象
    #返回值：游标对象
    @classmethod
    def get_cursor(cls,conn):
        return conn.cursor()

    #获取资源释放的函数
    #参数：cursor/conn
    #返回值：无
    @classmethod
    def close_res(cls,cursor,conn):
        #加入None判断
        if cursor:
            cursor.close()
            cursor=None
        if conn:
            conn.close()
            conn=None