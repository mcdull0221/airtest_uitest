# -*- coding: utf-8 -*-
import configparser
import os
from Base import BaseSetting


class BaseCommon:
    """
    获取env 配置
    """
    def __init__(self):
        self.cp = configparser.ConfigParser()
        self.__env = self._env()
        self.__app_name = self._app_name()
        self.__platform_name = self._platform_name()

    def _env(self):
        return self._get_env('env', 'env')

    def _app_name(self):
        return self._get_env('app', 'app_name')

    def _platform_name(self):
        return self._get_env('app_platform', 'platform_name')

    def _get_run_device_sum(self):
        return int(self._get_env('connect_device', 'run_device_num'))

    def _new_app_path(self):
        return self._get_env(self.__app_name, self.__env+'_'+self.__platform_name+'_new_app')

    def _old_app_path(self):
        return self._get_env(self.__app_name, self.__env+'_'+self.__platform_name+'_old_app')

    def _package_name(self):
        return self._get_env(self.__app_name, self.__env+'_'+self.__platform_name+'_package_name')

    def _activity_name(self):
        if self.__platform_name == 'android':
            return self._get_env(self.__app_name, self.__env+'_'+self.__platform_name+'_activity_name')

    def _get_env(self, tag_name, var_name):
        return self._get('env.ini', tag_name, var_name)

    # def _get_result_by_app(self, result_list):
    #     if len(result_list) == 1:
    #         result = result_list[0]
    #     elif len(result_list) > 1:
    #         if self.__app_name == 'skyvpn':
    #             result = result_list[0]
    #         elif self.__app_name == 'highvpn':
    #             result = result_list[1]
    #         elif self.__app_name == 'bitvpn':
    #             result = result_list[2]
    #     return result

    # def _get_account_user(self,var_name):
    #     """
    #     获取测试账号
    #     :param var_name:
    #     :return:
    #     """
    #     var = self.__env + '_' + var_name
    #     return self._get_account_ini('test_user', var)

    # def _get_account_ini(self, tag_name, var_name):
    #     result_list = self._get(self.__platform_name+'_account.ini', tag_name, var_name).split(',,')
    #     result = self._get_result_by_app(result_list)
    #     return result


    def _get_device(self, device, var_name):
        if self.__platform_name == 'android':
            tag_name = 'android_device'
        else:
            tag_name = 'ios_device'
        var = device+'_'+var_name
        return self._get_env(tag_name, var)

    def _get(self, file_name, tag_name, var_name):
        self.cp.read(os.path.join(BaseSetting.configDIR, file_name), encoding='utf-8')
        return self.cp.get(tag_name, var_name)

    def _get_element_ini(self, tag_name, var_name):
        element_ini_path = os.path.join(os.path.join(os.path.join(BaseSetting.ElementDir, self.__app_name),
                                                     self.__platform_name), 'LocalElement.ini')
        self.cp.read(element_ini_path, encoding='utf-8')
        return self.cp.get(tag_name, var_name)


if __name__ == '__main__':
    print(BaseCommon()._old_app_path())
    print(BaseCommon()._new_app_path())
    'device_1_udid '
    # print(BaseCommon()._get_device('device_1', 'udid'))
    # print(os.path.join(os.path.join(BaseSetting.ElementDir, 'skyvpn/'), 'android/'))
    # print(BaseCommon()._get_element_ini('MainActivity', 'Connect_Button'))
