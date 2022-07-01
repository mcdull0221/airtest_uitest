import os


BaseDIR = os.path.dirname(os.path.dirname(__file__))
Entrance_DIR = os.path.join(BaseDIR, "Entrance/")
static_DIR = os.path.join(Entrance_DIR, "static/")
configDIR = os.path.join(BaseDIR, "config/")
TestDataDIR = os.path.join(static_DIR, "TestData/")

CaseDIR = os.path.join(BaseDIR, "TestCase/")
LogsDIR = os.path.join(static_DIR, "Logs/")
PictureDir = os.path.join(TestDataDIR, "picture/")
ReportDIR = os.path.join(static_DIR, "Report/")

AppPath = os.path.join(BaseDIR, "apps/")
ElementDir = os.path.join(BaseDIR, "Element/")
# flask 登陆账号
USERNAME = "admin"
PD = "admin"
flask_port = 5001

# windows 兼容性
Entrance_DIR2 = Entrance_DIR.replace("/", "\\").replace("\\", "\\\\")

import socket
# 获取本机计算机名称
hostname = socket.gethostname()
# 获取本机ip
ip = socket.gethostbyname(hostname)

ipport = "http://"+ip+":" + str(flask_port) +"/"
ipport_REPORT_DIR = ipport+"static/Report/"

AirResource = ipport+"static/AirResource/"

if __name__ == '__main__':
    print(os.path.sep)
    print(ipport_REPORT_DIR)
    print(Entrance_DIR)
    print(CaseDIR + 'skyvpn' + '/' + 'android' + '/')
