# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def test_sendMail():
    # 声明用来登录的邮箱和口令
    password = 'sdjxhqksmlfsbghd'  # 发信授权码
    smtp_server = 'smtp.qq.com'  # 发信服务器

    sender = '467563369@qq.com'
    receivers = '467563369@qq.com'  # ['467563369@qq.com','a1804536661@qq.com']        # 接收邮箱

    # 邮箱正文 ，三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    # message = MIMEText('Python sendmail test', 'plain', 'utf-8')
    message = MIMEMultipart('related')

    # 邮件头信息
    message['From'] = Header('Test_sender', 'utf-8')  # 发送者
    message['To'] = Header('receivers', 'utf-8')  # 接收者
    message['Subject'] = Header('Python Email Subject', 'utf-8')

    # msgAlternative = MIMEMultipart('alternative')
    # message.attach(msgAlternative)

    mail_msg = """
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
    <p>图片演示：</p>
    <p><img src="cid:image1"></p>
    """
    message.attach(mail_msg)

    file = open('test.png', 'rb')
    img_data = file.read()
    file.close()

    img=MIMEImage(img_data)
    img.add_header('Content-ID','image1')
    message.attach(img)


    try:
        # 开启发信服务，这里使用的是加密传输
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(smtp_server, 465)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("send mail success")
    except smtplib.SMTPException:
        print("Error: can not send the mail")
    finally:
        # 关闭服务器
        smtpObj.quit()
