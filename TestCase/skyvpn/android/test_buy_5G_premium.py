# -*- encoding=utf8 -*-
from Base.BaseTestCase import BaseTestCase
from airtest.core.api import *
from Base.PublicFunction import *
from Base.BaseElement import *


class TestBuy5gPremium(BaseTestCase):

    def setUp(self):
        if self.poco(element('WelcomeActivity', 'Get_Start')).exists():  # get start 按钮
            self.poco(element('WelcomeActivity', 'Get_Start')).click()
            self.poco(element('MainActivity', 'Connect_Button')).wait(timeout=120)
            sleep()

    @frame("buy_5g_premium", "buy_5g_premium.html", "测试购买 5G premium 流量")
    def test_buy_5g_premium(self):
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
        before_traffic = int(self.poco(element('GetCreditsActivity', 'My_Balance')).get_text().split('M')[0])  # 任务页面流量
        traffic_list = self.poco(element('GetCreditsActivity', 'Task_List'))  # 任务列表
        # if not traffic_list.exists():
        #     self.poco.scroll(direction='vertical', percent=0.6, duration=1.0)
        #     while True:
        #         title = self.poco(element('GetCreditsActivity', 'Task_title'))[-1].get_text()
        #         print(title)
        #         if title != 'Purchase 5GB':
        #             self.poco(element('GetCreditsActivity', 'Task_List')).swipe([-0.0093, -0.6629])
        #             continue
        #         else:
        #             break
        while True:
            if not traffic_list.exists():
                self.poco.scroll(direction='vertical', percent=0.6, duration=1.0)
                continue
            else:
                title = self.poco(element('GetCreditsActivity', 'Task_title'))[-1].get_text()
                print(title)
                if title != 'Purchase 5GB':
                    self.poco.scroll(direction='vertical', percent=0.6, duration=1.0)
                    continue
                else:
                    break

        self.poco(element('GetCreditsActivity', 'Task_title'))[-1].click()
        sleep()
        self.poco(element('GoogleActivity', '5g_Buy_Button')).wait(timeout=20).click()

        # 等待购买完成
        self.poco(element('GetCreditsActivity', 'Sub_Loading')).wait_for_appearance()
        while True:
            sleep(3)
            if self.poco(element('GetCreditsActivity', 'Sub_Loading')).exists():
                continue
            else:
                break

        # 校验流量
        if not self.poco(element('GetCreditsActivity', 'My_Balance')).exists():
            while True:
                self.poco(element('GetCreditsActivity', 'Task_List')).swipe([0.0464, 0.811])
                sleep()
                if self.poco(element('GetCreditsActivity', 'My_Balance')).exists():
                    break
                else:
                    continue
        after_traffic = int(self.poco(element('GetCreditsActivity', 'My_Balance')).get_text().split('M')[0])
        assert_equal(after_traffic - before_traffic, 5120, "检查购买5G流量")
