# -*- encoding=utf8 -*-
from Base.BaseTestCase import BaseTestCase
from airtest.core.api import *
from Base.PublicFunction import *
from Base.BaseElement import *


class TestConnect(BaseTestCase):

    def setUp(self):
        # 在此之前要登录一个会员账号
        if self.poco(element('WelcomeActivity', 'Get_Start')).exists():  # get start 按钮
            self.poco(element('WelcomeActivity', 'Get_Start')).click()
            sleep(3)

        self.poco(element('MainActivity', 'Connect_Button')).wait(timeout=120)
        self.poco(element('MainActivity', 'Menu')).click()
        sleep()
        self.poco(element('MainActivity', 'Log_in')).click()
        sleep()
        self.poco(element('LoginActivity', 'Email_address')).set_text('sky01@qq.com')  # 登录账号
        sleep()
        self.poco(element('LoginActivity', 'Password')).set_text('123456')  # 登录密码
        sleep()
        self.poco(element('LoginActivity', 'Login')).click()  # 登录按钮
        sleep()
        self.poco(element('MainActivity', 'User_email')).wait(timeout=120)
        sleep()
        self.poco.scroll(direction='horizontal', percent=0.8, duration=0.5)
        sleep()

    @frame("connect", "connect.html", "测试连接服务器")
    def test_connect_server(self):
        """
        连接前要先判断权限，
        安卓连接有 BUG，首次连接无法连接成功
        """
        connect = element('MainActivity', 'Connect_Button')
        disconnect = element('MainActivity', 'DisConnect_Button')
        self.poco(connect).click()
        if exists(Template(PictureDir + "skyvpn_android_main_activity_vpn_permission_desc.png")):
            touch(Template(PictureDir + "skyvpn_android_main_activity_vpn_permission_ok.png"))
        sleep(5)

        rsp = self.poco.wait_for_any([self.poco(connect), self.poco(disconnect)])
        if rsp:
            rsp.click()
            sleep()

        self.poco(element('MainActivity', 'Server_Button')).click()   # 首页 server 入口
        sleep()
        frozen_serverlist = self.poco.freeze()
        # print(type(frozen_serverlist))
        # hierarchy_dict = frozen_serverlist.agent.hierarchy.dump()  # 字典类型
        # 国家列表
        server_list = frozen_serverlist(element('CountrysActivity', 'Server_list')).children()
        for i in range(1, len(server_list) - 1):
            server_list[i].click()
            sleep()
            self.poco(connect).click()
            wait(Template(PictureDir + "skyvpn_android_main_activity_connect_success.png"), timeout=120)
            sleep()
            self.poco(disconnect).click()
            sleep()
            country_name = self.poco(element('MainActivity', 'Country_name')).get_text()
            print("当前连接的contry---" + country_name)
            self.poco(element('MainActivity', 'Server_Button')).click()
            sleep()
