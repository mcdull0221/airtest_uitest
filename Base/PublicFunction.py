from airtest.core.helper import log

from Base.lib import *


def frame(log_name, report_name, case_desc=""):
    """
    用例装饰器
    :param log_name: 输出日志文件夹
    :param report_name: 报告文件名称
    :param case_desc: 用例描述
    :return:
    """
    def outer(func):
        def inner(self, *args, **kwargs):
            self.__dict__['_testMethodDoc'] = case_desc
            only_set_logdir(LogsDIR + log_name)
            try:
                f = func(self, *args, **kwargs)

            except Exception as e:
                print(e)
                log(e, "出错了", snapshot=True)
                raise e
            finally:
                DIY_simple_report(__file__, logpath=LogsDIR + log_name, output=ReportDIR + report_name)
                print("输出报告")
                self.__dict__['_html_path'] = ipport_REPORT_DIR + report_name
            return f
        return inner
    return outer


