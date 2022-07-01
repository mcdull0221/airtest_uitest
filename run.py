import configparser
import os
import sys
import unittest
from Base.lib import generate_report
from Base.BaseSetting import static_DIR, CaseDIR, ReportDIR, configDIR
from Base.BeautifulLib import DIYBeautifulReport
from TestCase.skyvpn.android.test_buy_5G_premium import TestBuy5gPremium
from TestCase.skyvpn.android.test_checkin import TestCheckIn
from TestCase.skyvpn.android.test_feel_lucky import TestFeelingLucky
from TestCase.skyvpn.android.test_login import TestLogin
from TestCase.skyvpn.android.test_login_code_refresh import TestLoginCodeRefresh
from TestCase.skyvpn.android.test_none_basic_connect import TestNoneBasicConnect
from TestCase.skyvpn.android.test_overwrite_installation import TestOverwriteInstallation
from TestCase.skyvpn.android.test_sign_up_fail import TestSignUpFail
from TestCase.skyvpn.android.test_sign_up_success import TestSignUpSuccess
from TestCase.skyvpn.android.test_term_of_service import TestTermOfService


def modify_env_config(app, env, platform):
    config_env_file = os.path.join(configDIR, 'env.ini')
    cp = configparser.ConfigParser()
    cp.read(config_env_file)
    cp.set('env', 'env', env)
    cp.set('app', 'app_name', app)
    cp.set('app_platform', 'platform_name', platform)
    cp.write(open(config_env_file, 'w'))


def get_case(app, platform):
    testloader = unittest.TestLoader()
    # suite = testloader.discover(CaseDIR + app + '/' + platform + '/')
    suite = testloader.loadTestsFromTestCase(TestNoneBasicConnect)

    print('case path===' + CaseDIR + app + '/' + platform + '/')
    return suite


def run_case(app, platform):
    suite = get_case(app, platform)
    runner = DIYBeautifulReport(suite)
    runner.report("UI自动化测试报告", "report.html", report_dir=static_DIR)


def main(app, environment, platform):
    generate_report(ReportDIR)
    modify_env_config(app, environment, platform)

    run_case(app, platform)
    # todo 增加报告的通知


if __name__ == '__main__':
    # 做了下判断对输入参数数量不符合的时候直接退出程序
    if len(sys.argv) != 4:
        sys.exit()
    print(sys.argv)
    # skyvpn or coverme
    app = sys.argv[1]

    # dn1 or pn1
    environment = sys.argv[2]

    # 操作系统 ios  or android
    platform = sys.argv[3]

    main(app, environment, platform)
    # todo 尝试增加并发和失败重跑
