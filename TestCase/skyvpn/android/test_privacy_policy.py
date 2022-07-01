# -*- encoding=utf8 -*-
from Base.BaseTestCase import BaseTestCase
from airtest.core.api import *
from Base.PublicFunction import *
from Base.BaseElement import *


class TestPrivacyPolicy(BaseTestCase):

    def setUp(self):
        if self.poco(element('WelcomeActivity', 'Get_Start')).exists():  # get start 按钮
            self.poco(element('WelcomeActivity', 'Get_Start')).click()
            self.poco(element('MainActivity', 'Connect_Button')).wait(timeout=120)
            sleep()

    @frame("privacy_policy", "privacy_policy.html", "测试隐私政策是否能正常打开")
    def test_privacy_policy(self):
        # 判断模式，进入任务
        self.poco(element('MainActivity', 'Menu')).click()
        sleep()
        self.poco(element('MainActivity', 'Help')).click()
        sleep(2)
        self.poco(element('HelpActivity', 'Privacy_policy')).click()
        sleep(6)
        assert_exists(Template(PictureDir + "skyvpn_android_web_privacy_policy.png"), "跳转成功")
