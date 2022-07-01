# -*- encoding=utf8 -*-
from airtest.core.api import *
from Base.BaseCommon import BaseCommon


class BaseConnect(BaseCommon):
    def __init__(self):
        BaseCommon.__init__(self)
        self.platform = self.get_platform()
        self.num = BaseCommon()._get_run_device_sum()
        self.device_list = []

    def get_device(self):
        for i in range(1, self.num+1):
            device_id = self._get_device('device_'+str(i), 'udid')
            if device_id is not None:
                if self.platform == 'android':
                    devices = self.platform + ':///' + device_id + '?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH'
                    self.device_list.append(devices)
                else:
                    devices = self.platform + ':///' + device_id
                    self.device_list.append(devices)
        print(self.device_list)

    def base_driver(self):
        self.get_device()
        auto_setup(__file__, logdir=None, devices=self.device_list)

    def get_platform(self):
        return self._platform_name()

    def get_package_name(self):
        return self._package_name()

    def start_poco(self):
        if self.platform == 'android':
            # 初始化android poco
            from poco.drivers.android.uiautomation import AndroidUiautomationPoco
            poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
            poco("<Root>")
        else:
            # 初始化 iOS poco
            from poco.drivers.ios import iosPoco
            poco = iosPoco()
        return poco


if __name__ == '__main__':
    # for i in range(1, 4):
    #     print(i)
    BaseConnect().get_device()
    print(BaseConnect()._package_name())
