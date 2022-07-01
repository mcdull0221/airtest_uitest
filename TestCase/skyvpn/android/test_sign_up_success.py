# -*- encoding=utf8 -*-
from Base.BaseTestCase import BaseTestCase
from airtest.core.api import *
from Base.PublicFunction import *
from Base.BaseElement import *


class TestSignUpSuccess(BaseTestCase):

    def setUp(self):
        if self.poco(element('WelcomeActivity', 'Get_Start')).exists():  # get start 按钮
            self.poco(element('WelcomeActivity', 'Get_Start')).click()
            self.poco(element('MainActivity', 'Connect_Button')).wait(timeout=120)
            sleep()

    @frame("sign_up_success", "sign_up_success.html", "测试注册账号成功")
    def test_sign_up_success(self):
        self.poco(element('MainActivity', 'Menu')).click()
        sleep()
        self.poco(element('MainActivity', 'Register')).click()
        sleep(2)
        account = str(int(time.time())) + "@testaccount.com"
        self.poco(element('RegisterActivity', 'Email_address')).wait().set_text(account)
        sleep()
        self.poco(element('RegisterActivity', 'Password')).set_text('123456')
        sleep()
        self.poco(element('RegisterActivity', 'Sign_up')).click()
        sleep()
        self.poco(element('RegisterActivity', 'Confirm_register_sure')).wait().click()
        sleep(3)
        self.poco(element('MainActivity', 'Menu_Subscribe')).wait(timeout=60)
        log('注册成功进入首页', snapshot=True)
        is_register = self.poco(element('MainActivity', 'User_email')).exists()
        assert_equal(True, is_register, '判断是否注册成功')
