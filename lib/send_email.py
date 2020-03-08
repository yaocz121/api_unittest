import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
from config.config import *

def send_email(report_file):
    msg = MIMEMultipart() #混合MIME模式
    msg.attach(MIMEText(open(report_file,encoding='utf-8').read(),'html','utf-8'))
    #组装Email头(发送人，收件人，主题)
    msg['From'] = 'yaoczz@foxmail.com'
    msg['To'] = 'yaoczz@foxmail.com'
    #中文邮件主题，指定utf-8编码
    msg['Subject'] = Header(subject,'utf-8')
    #构造附件
    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 从配置文件中读取
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="{}"'.format(os.path.basename(report_file))  # 参数化一下report_file
    msg.attach(att1)
    try:
        smtp = smtplib.SMTP_SSL(smtp_server)  # 从配置文件中读取
        smtp.login(smtp_user, smtp_password)  # 从配置文件中读取
        smtp.sendmail(sender, receiver, msg.as_string())
        logging.info("邮件发送完成！")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()
