import logging
import os
import time
from optparse import OptionParser

today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M%S',time.localtime())

#项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#数据目录
data_path = os.path.join(prj_path,'data')

#用例目录
test_case_path  = os.path.join(prj_path,'test','case')

log_file = os.path.join(prj_path,'log','log_{}.txt'.format(today))

report_file = os.path.join(prj_path,'report','report_{}.html'.format(now))

data_file = os.path.join(prj_path, 'data', 'test_user_data.xlsx')

last_fails_file = os.path.join(prj_path, 'failures_test.pickle')

#邮件开关
send_email_after_run = True


logging.basicConfig(level=logging.DEBUG,
    format= '[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
    datefmt= '%Y-%m-%d %H:%M:%S',
    filename=log_file,
    filemode='a'

)



#邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = 'username'
smtp_password = 'password'

sender = smtp_user
receiver = '接收人地址''
subject = '接口测试报告'


