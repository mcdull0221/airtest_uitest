import os
import shutil
import wget
from Base.BaseCommon import BaseCommon
from Base.BaseSetting import AppPath


class DownloadApp(BaseCommon):
    def __init__(self):
        BaseCommon.__init__(self)
        self.platform = self._platform_name()
        self.app_name = self._app_name()
        self.new_app_path = self.get_new_app_path()
        self.old_app_path = self.get_old_app_path()
        self.app_path = self.get_app_path()
        # /Users/tengzhan/Desktop/test/apps/skyvpn/android

    def clear_path(self):
        if os.path.exists(self.app_path):
            shutil.rmtree(self.app_path)
        os.makedirs(self.app_path, exist_ok=True)

    @staticmethod
    def get_new_app_path():
        # 获取app 新版本下载路径
        return BaseCommon()._new_app_path()

    @staticmethod
    def get_old_app_path():
        # 获取app 旧版本下载路径
        return BaseCommon()._old_app_path()

    def get_app_path(self):
        # 获取app 存放路径
        return os.path.join(os.path.join(AppPath, self.app_name), self.platform)

    def download_new_app(self):
        if self.platform == 'android':
            wget.download(self.new_app_path, os.path.join(self.app_path, "new.apk"))
        else:
            wget.download(self.new_app_path, os.path.join(self.app_path, "new.app"))
        print("==app download complete==")

    def download_old_app(self):
        if self.platform == 'android':
            wget.download(self.old_app_path, os.path.join(self.app_path, "old.apk"))
        else:
            wget.download(self.old_app_path, os.path.join(self.app_path, "old.app"))
        print("==app download complete==")

    def download_app(self):
        self.clear_path()
        self.download_old_app()
        self.download_new_app()


if __name__ == '__main__':
    print(DownloadApp().old_app_path)
    DownloadApp().clear_path()
