# -*- encoding=utf8 -*-
from Base.BaseTestCase import BaseTestCase
from airtest.core.api import *
from Base.PublicFunction import *
from Base.BaseElement import *


class TestLoginCodeRefresh(BaseTestCase):

    def setUp(self):
        if self.poco(element('WelcomeActivity', 'Get_Start')).exists():  # get start 按钮
            self.poco(element('WelcomeActivity', 'Get_Start')).click()
            self.poco(element('MainActivity', 'Connect_Button')).wait(timeout=120)
            sleep()

    @frame("login_code_refresh", "login_code_refresh.html", "测试5码刷新")
    def test_login_code_refresh(self):
        # 判断模式，进入任务
        self.poco(element('MainActivity', 'Menu')).click()
        sleep()
        self.poco(element('MainActivity', 'PC_Mac')).click()
        sleep(5)
        code_before = self.poco(element('CodeLoginActivity', 'Login_Code')).get_text()
        self.poco(element('CodeLoginActivity', 'Code_Refresh')).click()
        sleep(5)
        code_after = self.poco(element('CodeLoginActivity', 'Login_Code')).get_text()
        assert_not_equal(code_before, code_after, "判断无码刷新后前后2次不一样")
