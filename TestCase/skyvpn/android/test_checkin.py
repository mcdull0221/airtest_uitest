# -*- encoding=utf8 -*-
from Base.BaseConnect import BaseConnect
from Base.BaseTestCase import BaseTestCase
from airtest.core.api import *
from Base.PublicFunction import *
from Base.BaseElement import *


class TestCheckIn(BaseTestCase):

    def setUp(self):
        if self.poco(element('WelcomeActivity', 'Get_Start')).exists():  # get start 按钮
            self.poco(element('WelcomeActivity', 'Get_Start')).click()
            self.poco(element('MainActivity', 'Connect_Button')).wait(timeout=120)
            sleep()

    @frame("check_in", "check_in.html", "测试check_in")
    def test_check_in(self):
        # 1. 测试 check_in
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
            check_in = exists(Template(PictureDir + "skyvpn_android_getcredits_activity_checkin_btn.png"))
            if check_in:
                touch(check_in)
                sleep()
                break
            elif not check_in:
                self.poco.scroll(direction='vertical', percent=0.6, duration=1.0)
                i += 1
                continue
            elif i == 3:
                log("未找到 check_in", snapshot=True)
                break
        if self.poco(element('GetCreditsActivity', 'Checkin_AD_close')).exists():
            self.poco(element('GetCreditsActivity', 'Checkin_AD_close')).click()

        self.poco(element('GetCreditsActivity', 'Checkin')).wait(timeout=10).click()
        sleep()
        assert_exists(Template(PictureDir + "skyvpn_android_getcredits_activity_checkin_success.png"),
                      "check_in 成功")

        stop_app(BaseConnect().get_package_name())
        sleep()

        # 2. 测试已经 check_in 过了
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
            check_in = exists(Template(PictureDir + "skyvpn_android_getcredits_activity_checkin_btn.png"))
            if check_in:
                touch(check_in)
                sleep()
                break
            elif not check_in:
                self.poco.scroll(direction='vertical', percent=0.6, duration=1.0)
                i += 1
                continue
            elif i == 3:
                log("未找到 check_in", snapshot=True)
                break
        if self.poco(element('GetCreditsActivity', 'Checkin_AD_close')).exists():
            self.poco(element('GetCreditsActivity', 'Checkin_AD_close')).click()

        self.poco(element('GetCreditsActivity', 'Checkin')).wait(timeout=10).click()
        sleep()
        self.poco(element('GetCreditsActivity', 'Checkin_AD_loading')).wait(timeout=10)

        assert_exists(Template(PictureDir + "skyvpn_android_getcredits_activity_checkin_done.png"),
                      "check_in 成功")
