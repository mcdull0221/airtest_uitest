# -*- encoding=utf8 -*-
from airtest.core.api import *
import unittest
import logging
from Base.BaseConnect import BaseConnect


class BaseTestCase(unittest.TestCase):
    # 测试方法基类
    @classmethod
    def setUpClass(cls, platform='android'):
        super(BaseTestCase, cls).setUpClass()
        # 设置日志等级
        logger = logging.getLogger("airtest")
        logger.setLevel(logging.ERROR)
        # 初始化设备
        BaseConnect().base_driver()
        clear_app(BaseConnect().get_package_name())
        sleep()
        start_app(BaseConnect().get_package_name())
        sleep(5)

        print("--start--")
        # from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        # cls.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        # cls.poco("<Root>")
        cls.poco = BaseConnect().start_poco()
        sleep(4)

    # def setUp(self):
    #     # 初始化设备
    #     BaseConnect().base_driver()
    #     clear_app(BaseConnect().get_package_name())
    #     sleep()
    #     start_app(BaseConnect().get_package_name())
    #     sleep(5)
    #
    # def tearDown(self):
    #     stop_app(BaseConnect().get_package_name())

    @classmethod
    def tearDownClass(cls):
        # from airtest.core.android.adb import cleanup_adb_forward
        # cleanup_adb_forward()
        # print("移除adb forward")
        stop_app(BaseConnect().get_package_name())
        sleep(4)

