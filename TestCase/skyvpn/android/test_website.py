# -*- encoding=utf8 -*-
from Base.BaseTestCase import BaseTestCase
from airtest.core.api import *
from Base.PublicFunction import *
from Base.BaseElement import *


class TestWebsite(BaseTestCase):

    def setUp(self):
        if self.poco(element('WelcomeActivity', 'Get_Start')).exists():  # get start 按钮
            self.poco(element('WelcomeActivity', 'Get_Start')).click()
            self.poco(element('MainActivity', 'Connect_Button')).wait(timeout=120)
            sleep()

    @frame("Website", "Website.html", "测试官网是否能正常打开")
    def test_Website(self):
        # 判断模式，进入任务
        self.poco(element('MainActivity', 'Menu')).click()
        sleep()
        self.poco(element('MainActivity', 'Help')).click()
        sleep(2)
        self.poco(element('HelpActivity', 'Website')).click()
        sleep(6)
        assert_exists(Template(PictureDir + "skyvpn_android_web_website.png"), "跳转成功")
