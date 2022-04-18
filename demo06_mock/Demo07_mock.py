#需求：测试购物车接口，但是需要先调用登录接口（登录实现比较复杂：需要录入手机号码，已经服务器发送的验证码）
#实现：
#1、需要实现导入unnitest
import unittest
from unittest import mock
#2、确定被模拟的接口
#登录函数   需要参数：手机号+验证码   返回值：True/False
def login(tel,verify_code):
    #验证手机号和服务器发送的验证码是否匹配，是返回true，否则返回false
    #....
    return False

class TestLogin(unittest.TestCase):
    #测试登录函数
    def test_cart(self):
        #3、创建mock服务
        login = mock.Mock(return_value=True) #设置预期的返回结果
        #4、并且调用mock服务
        #a、先登录
        result = login("110","8888","1234")
        #b、测试购物车
        #....
        #添加断言，判断登录结果
        print("登录结果：",result)
        self.assertEqual(True,result)
