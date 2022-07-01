# -*- encoding=utf8 -*-
from Base.BaseTestCase import BaseTestCase
from airtest.core.api import *
from Base.PublicFunction import *
from Base.BaseElement import *


class TestSignUpFail(BaseTestCase):

    def setUp(self):
        if self.poco(element('WelcomeActivity', 'Get_Start')).exists():  # get start 按钮
            self.poco(element('WelcomeActivity', 'Get_Start')).click()
            self.poco(element('MainActivity', 'Connect_Button')).wait(timeout=120)
            sleep()

    @frame("sign_up_fail", "sign_up_fail.html", "测试注册账号失败")
    def test_sign_up_fail(self):
        self.poco(element('MainActivity', 'Menu')).click()
        sleep()
        self.poco(element('MainActivity', 'Register')).click()
        sleep(2)
        account = "sky01@qq.com"
        self.poco(element('RegisterActivity', 'Email_address')).wait().set_text(account)
        sleep()
        self.poco(element('RegisterActivity', 'Password')).set_text('123456')
        sleep()
        self.poco(element('RegisterActivity', 'Sign_up')).click()
        sleep()
        # 弹出已注册弹框
        self.poco(element('RegisterActivity', 'Confirm_register_sure')).wait()
        log('注册失败弹框', snapshot=True)
        sleep()
        confirm_msg = self.poco(element('RegisterActivity', 'Confirm_register_msg')).get_text()
        assert_equal('This email address has already been registered.', confirm_msg, '判断已注册的账号注册提示是否正确')
