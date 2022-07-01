# -*- encoding=utf8 -*-
from Base.BaseTestCase import BaseTestCase
from airtest.core.api import *
from Base.PublicFunction import *
from Base.BaseElement import *


class TestNoneBasicConnect(BaseTestCase):

    def setUp(self):
        if self.poco(element('WelcomeActivity', 'Get_Start')).exists():  # get start 按钮
            self.poco(element('WelcomeActivity', 'Get_Start')).click()
            sleep(3)

        self.poco(element('MainActivity', 'Connect_Button')).wait(timeout=120)
        self.poco(element('MainActivity', 'Menu')).click()
        sleep()
        self.poco(element('MainActivity', 'Log_in')).click()
        sleep()
        self.poco(element('LoginActivity', 'Email_address')).set_text('skybasic0@qq.com')  # 登录账号
        sleep()
        self.poco(element('LoginActivity', 'Password')).set_text('123456')  # 登录密码
        sleep()
        self.poco(element('LoginActivity', 'Login')).click()  # 登录按钮
        sleep()
        self.poco(element('MainActivity', 'User_email')).wait(timeout=120)
        sleep()
        self.poco.scroll(direction='horizontal', percent=0.8, duration=0.5)
        sleep()

    @frame("none_basic_connect", "none_basic_connect.html", "测试没有basic 流量 连接 basic")
    def test_none_basic_connect(self):
        """
        连接前要先判断权限，
        """
        # 判断模式
        mode = self.poco(element('MainActivity', 'Use_mode')).get_text()
        if mode == 'Premium':
            self.poco(element('MainActivity', 'Use_mode')).click()
            sleep()
            self.poco(element('MainActivity', 'Basic_mode')).click()
            sleep()
            self.poco(element('MainActivity', 'Switch_basic')).click()
            sleep()
        elif mode == 'Basic':
            pass
        else:
            print("模式不对，请检查")

        self.poco(element('MainActivity', 'Connect_Button')).click()
        if exists(Template(PictureDir + "skyvpn_android_main_activity_vpn_permission_desc.png")):
            touch(Template(PictureDir + "skyvpn_android_main_activity_vpn_permission_ok.png"))
            rsp = self.poco.wait_for_any([self.poco(element('MainActivity', 'Connect_Button')),
                                          self.poco(element('MainActivity', 'DisConnect_Button'))])
            if rsp:
                rsp.click()
                sleep()
            self.poco(element('MainActivity', 'Connect_Button')).click()
        sleep(3)

        assert_exists(Template(PictureDir + "skyvpn_android_main_activity_no_basic_connect_dialog.png"),
                      "无basic 流量正常弹框")
