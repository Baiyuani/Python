from email.mime.text import MIMEText
from email.header import Header
import smtplib
from getpass import getpass


def send_email(body, sender, receivers, subject, server, passwd):
    # 准备邮件,plain表示纯文本邮件
    msg = MIMEText(body, 'plain', 'utf8')
    msg['From'] = Header(sender, 'utf8')
    msg['To'] = Header(receivers[0], 'utf8')
    msg['Subject'] = Header(subject)

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(server)
    # smtp.starttls()  # 类似于https，如果服务器要求加密，则启用此语句
    smtp.login(sender, passwd)
    smtp.sendmail(sender, receivers, msg.as_bytes())


if __name__ == '__main__':
    body = 'Python发送邮件测试\n'
    sender = '1036354613@qq.com'
    receivers = ['13835518617@163.com', '1036354613@qq.com']
    subject = 'py test'
    server = 'smtp.qq.com'
    passwd = getpass()
    send_email(body, sender, receivers, subject, server, passwd)
