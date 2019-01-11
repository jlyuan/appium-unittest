import datetime
import os

NOW = datetime.datetime.now()

# 项目根目录
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试用例目录
TEST_CASE_ROOT = os.path.join(PROJECT_PATH, 'TestCase')
# 测试报告目录
REPORT_PATH = os.path.join(PROJECT_PATH, 'report')
# 测试报告HTML文件
REPORT_HTML_PATH = os.path.join(REPORT_PATH, 'TestReport.html')
# 屏幕截图存储路径
SCREEN_SHOT_PATH = os.path.join(REPORT_PATH, 'screen-shot', NOW.date().__str__())
# log文件存放目录
LOG_FILE_PATH = os.path.join(REPORT_PATH, 'log')
# 预置文件存放目录
RESOURCE_FILE_PATH = os.path.join(PROJECT_PATH, 'resource')

STATIC_FILE_PATH = os.path.join(PROJECT_PATH, 'Resources')
EMAIL_REPORT_HTML_TPL = os.path.join(STATIC_FILE_PATH, 'email_report_tpl', 'ci_report.html')
# 公共邮箱
# 登录密码：hfx@2018
EMAIL = dict(
    SMTP_SERVER='smtp.163.com',
    SSL_PORT='465',
    USERNAME='cmcchefeixin@163.com',
    SMTP_PASSWORD='cmcc2018'
)
