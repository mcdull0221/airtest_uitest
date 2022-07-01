# -*- encoding=utf8 -*-
import unittest
from Base.BaseConnect import BaseConnect
from Base.BaseTestCase import BaseTestCase
from airtest.core.api import *
# from airtest.core.ios.ios import *
from Base.Download_app import DownloadApp
from Base.PublicFunction import *
from Base.BaseElement import *


class TestOverwriteInstallation(BaseTestCase):

    @classmethod
    def setUpClass(cls, platform='android'):
        # 初始化设备
        cls.download_app = DownloadApp()
        cls.download_app.download_app()
        BaseConnect().base_driver()
        cls.app_path = cls.download_app.get_app_path()
        cls.package_name = BaseConnect().get_package_name()
        if BaseConnect().get_platform() == 'android':
            from airtest.core.android import android
            android = android.Android()
            if android.check_app(cls.package_name):
                uninstall(cls.package_name)
            install(os.path.join(cls.app_path, "old.apk"))
        else:
            # from airtest.core.ios import ios
            # ios = ios.IOS()
            # ios.uninstall_app(package_name)
            # ios.install_app(download_app.get_old_app_path())
            pass
            # ios 先跳过覆盖安装case
        clear_app(cls.package_name)
        sleep()
        start_app(cls.package_name)
        sleep(5)

        print("--start--")
        cls.poco = BaseConnect().start_poco()
        sleep(4)

    def setUp(self):
        self.connect = element('MainActivity', 'Connect_Button')
        self.disconnect = element('MainActivity', 'DisConnect_Button')
        if self.poco(element('WelcomeActivity', 'Get_Start')).exists():  # get start 按钮
            self.poco(element('WelcomeActivity', 'Get_Start')).click()
            self.poco(self.connect).wait()
            sleep()

    @unittest.skipIf(BaseConnect().get_platform() == 'ios', "ios 覆盖安装先不测试")
    @frame("overwrite_installation", "overwrite_installation.html", "测试覆盖安装")
    def test_overwrite_installation(self):
        self.poco(self.connect).click()
        if exists(Template(PictureDir + "skyvpn_android_main_activity_vpn_permission_desc.png")):
            touch(Template(PictureDir + "skyvpn_android_main_activity_vpn_permission_ok.png"))
        sleep(5)
        self.poco.wait_for_any([self.poco(self.connect), self.poco(self.disconnect)])

        # rsp = self.poco.wait_for_any([self.poco(self.connect), self.poco(self.disconnect)])
        # if rsp:
        #     rsp.click()
        #     sleep()

        install(os.path.join(self.app_path, "new.apk"))
        sleep()
        start_app(self.package_name)
        # 先登陆会员账号
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
        self.poco(element('MainActivity', 'Log_in')).wait(timeout=120)
        sleep()
        self.poco("me.skyvpn.app:id/scroll").swipe([-0.8153, 0.0091])
        sleep()

        self.poco(self.connect).wait(timeout=120).click()
        wait(Template(PictureDir + "skyvpn_android_main_activity_connect_success.png"), timeout=120)
        sleep()
        self.poco(self.disconnect).click()
        assert_exists(Template(PictureDir + "skyvpn_android_main_activity_connect.png"), '测试可用正常连接断开')

