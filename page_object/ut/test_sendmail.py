import smtplib
from email.mime.text import MIMEText
from email.header import Header

def test_sendMail():
    sender = '467563369@qq.com'
    password = 'sdjxhqksmlfsbghd'       # 发信授权码
    smtp_server = 'smtp.qq.com'         # 发信服务器

    receivers = '467563369@qq.com'#['467563369@qq.com','a1804536661@qq.com']        # 接收邮箱


    # 邮箱正文 ，三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('Python sendmail test','plain','utf-8')

    # 邮件头信息
    message['From'] = Header('sender','utf-8')    # 发送者
    message['To'] = Header('receivers','utf-8')       # 接收者
    message['Subject'] = Header('Python Email Subject','utf-8')

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender,receivers,message.as_string())
        print("send mail success")
    except smtplib.SMTPException:
        print("Error: can not send the mail")
    # 邮件头信息
    # message['From'] = Header(sender)
    # message['To'] = Header(receivers)
    # message['Subject'] = Header('python test')
    #
    # # 开启发信服务，这里使用的是加密传输
    # server = smtplib.SMTP_SSL()
    # server.connect(smtp_server, 465)
    # # 登录发信邮箱
    # server.login(sender, password)
    # # 发送邮件
    # server.sendmail(sender, receivers, message.as_string())
    # # 关闭服务器
    # server.quit()