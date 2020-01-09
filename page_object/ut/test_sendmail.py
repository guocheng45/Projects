# coding=utf-8
from datetime import datetime
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
    msg = MIMEMultipart('related')

    # 邮件头信息
    msg['From'] = Header('Test_sender', 'utf-8')  # 发送者
    msg['To'] = Header('receivers', 'utf-8')  # 接收者
    msg['Subject'] = Header('Python Email Subject', 'utf-8')

    # msgAlternative = MIMEMultipart('alternative')
    # message.attach(msgAlternative)

    mail_msg = MIMEText("""
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
    <p>图片演示：</p>
    <p><img src="cid:image1"></p>
    """,'html','utf-8')
    msg.attach(mail_msg)

    file = open('test.png', 'rb')
    img_data = file.read()
    file.close()

    img=MIMEImage(img_data)
    img.add_header('Content-ID','image1')
    msg.attach(img)


    try:
        # 开启发信服务，这里使用的是加密传输
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(smtp_server, 465)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receivers, msg.as_string())
        print("send mail success")
    except smtplib.SMTPException:
        print("Error: can not send the mail")
    finally:
        # 关闭服务器
        smtpObj.quit()

'''
from datetime import datetime
# 然后在需要的位置加上截图语句，文件路径自定义为自己本地路径   
driver.get_screenshot_as_file('/Users/hugo/Desktop/PythonStudy/%s.png'% datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3])
# strftime里面可以定义YMDHMSf（对应年月日时分秒，如不相太长，可以根据需要去掉年、月之类的），后面的[:-3是保留秒的后面3位]。
'''
def test_screenshorts():
    name = datetime.now().strftime("%Y%m%d%H%M%S")
    # driver.get_screenshot_as_file('D:\Projects\page_object\ut\%s.png' % name)
    print(name)