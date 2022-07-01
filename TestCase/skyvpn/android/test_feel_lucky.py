# -*- encoding=utf8 -*-
from Base.BaseConnect import BaseConnect
from Base.BaseTestCase import BaseTestCase
from airtest.core.api import *
from Base.PublicFunction import *
from Base.BaseElement import *


class TestFeelingLucky(BaseTestCase):

    def setUp(self):
        if self.poco(element('WelcomeActivity', 'Get_Start')).exists():  # get start 按钮
            self.poco(element('WelcomeActivity', 'Get_Start')).click()
            self.poco(element('MainActivity', 'Connect_Button')).wait(timeout=120)
            sleep()

    @frame("feeling_lucky", "feeling_lucky.html", "测试felling lucky")
    def test_feeling_lucky(self):
        # 1. 测试 felling lucky
        # 判断模式，进入任务
        mode = self.poco(element('MainActivity', 'Use_mode')).get_text()
        if mode == 'Basic':
            self.poco(element('MainActivity', 'Streamer')).click()
            sleep()
            self.poco(element('MainActivity', 'Streamer')).click()
        elif mode == 'Premium':
            self.poco(element('MainActivity', 'Streamer')).click()
        else:
            print("模式不对，请检查")

        sleep()
        # 进入任务页面需要判断一些弹框
        if self.poco(element('GetCreditsActivity', 'Geocaching_close')).exists():
            self.poco(element('GetCreditsActivity', 'Geocaching_close')).click()
        elif self.poco(element('GetCreditsActivity', 'AD_close')).exists():
            self.poco(element('GetCreditsActivity', 'AD_close')).click()
        sleep()

        while True:
            i = 0
            feeling_lucky = exists(Template(PictureDir + "skyvpn_android_getcredits_activity_feelinglucky_btn.png"))
            if feeling_lucky:
                touch(feeling_lucky)
                sleep(2)
                break
            elif not feeling_lucky:
                self.poco.scroll(direction='vertical', percent=0.6, duration=1.0)
                i += 1
                continue
            elif i == 3:
                log("未找到 felling luvky", snapshot=True)
                break

        assert_exists(Template(PictureDir + "skyvpn_android_getcredits_activity_feelinglucky_success.png"),
                      "felling lucky成功")
        stop_app(BaseConnect().get_package_name())
        sleep()

        # 2. 测试已经 fellinglucky 过了
        start_app(BaseConnect().get_package_name())
        sleep(4)
        mode = self.poco(element('MainActivity', 'Use_mode')).get_text()
        if mode == 'Basic':
            self.poco(element('MainActivity', 'Streamer')).click()
            sleep()
            self.poco(element('MainActivity', 'Streamer')).click()
        elif mode == 'Premium':
            self.poco(element('MainActivity', 'Streamer')).click()
        else:
            print("模式不对，请检查")

        sleep()
        # 进入任务页面需要判断一些弹框
        if self.poco(element('GetCreditsActivity', 'Geocaching_close')).exists():
            self.poco(element('GetCreditsActivity', 'Geocaching_close')).click()
        elif self.poco(element('GetCreditsActivity', 'AD_close')).exists():
            self.poco(element('GetCreditsActivity', 'AD_close')).click()
        sleep()

        while True:
            i = 0
            feeling_lucky = exists(Template(PictureDir + "skyvpn_android_getcredits_activity_feelinglucky_btn.png"))
            if feeling_lucky:
                touch(feeling_lucky)
                sleep(2)
                break
            elif not feeling_lucky:
                self.poco.scroll(direction='vertical', percent=0.6, duration=1.0)
                i += 1
                continue
            elif i == 3:
                log("未找到 felling luvky", snapshot=True)
                break
        assert_exists(Template(PictureDir + "skyvpn_android_getcredits_activity_feelinglucky_done.png"),
                      "已经felling lucky过，不能获得奖励")
