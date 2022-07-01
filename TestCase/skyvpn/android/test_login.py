# -*- encoding=utf8 -*-
from Base.BaseTestCase import BaseTestCase
from airtest.core.api import *
from Base.PublicFunction import *
from Base.BaseElement import *


class TestLogin(BaseTestCase):

    def setUp(self):
        if self.poco(element('WelcomeActivity', 'Get_Start')).exists():  # get start 按钮
            self.poco(element('WelcomeActivity', 'Get_Start')).click()
            self.poco(element('MainActivity', 'Connect_Button')).wait(timeout=120)
            sleep()

    @frame("login", "login.html", "测试账号登陆失败")
    def test_login(self):
        # 账号登陆成功在其他case有涉及，这里只测登录失败
        self.poco(element('MainActivity', 'Menu')).click()
        sleep()
        self.poco(element('MainActivity', 'Log_in')).click()
        sleep(2)
        self.poco(element('LoginActivity', 'Email_address')).wait().set_text('asjkdbhf@dfjn.test')
        sleep()
        self.poco(element('LoginActivity', 'Password')).set_text('xjndsdf')
        sleep()
        self.poco(element('LoginActivity', 'Login')).click()
        sleep(3)
        assert_exists(Template(PictureDir + "skyvpn_android_login_activity_login_failed.png"), "登录失败，显示提示")
