# -*- encoding=utf8 -*-
from Base.BaseTestCase import BaseTestCase
from airtest.core.api import *
from Base.PublicFunction import *
from Base.BaseElement import *


class TestTermOfService(BaseTestCase):

    def setUp(self):
        if self.poco(element('WelcomeActivity', 'Get_Start')).exists():  # get start 按钮
            self.poco(element('WelcomeActivity', 'Get_Start')).click()
            self.poco(element('MainActivity', 'Connect_Button')).wait(timeout=120)
            sleep()

    @frame("term_of_service", "term_of_service.html", "测试服务协议是否能正常打开")
    def test_term_of_service(self):
        # 判断模式，进入任务
        self.poco(element('MainActivity', 'Menu')).click()
        sleep()
        self.poco(element('MainActivity', 'Help')).click()
        sleep(2)
        self.poco(element('HelpActivity', 'Term_service')).click()
        sleep(6)
        assert_exists(Template(PictureDir + "skyvpn_android_web_terms_of_service.png"), "跳转成功")
