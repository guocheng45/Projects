# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class SendMail():
    def sendMail(self,msg1,pic,receiver):
        # 声明用来登录的邮箱和口令
        password = 'sdjxhqksmlfsbghd'  # 发信授权码
        smtp_server = 'smtp.qq.com'  # 发信服务器
        sender = '467563369@qq.com'
        receivers = ['467563369@qq.com','guozhicheng@ehaoyao.com']        # 接收邮箱

        msg = MIMEMultipart('related')
        # 邮件头信息
        msg['From'] = sender  # 发送者
        msg['To'] = ";".join(receivers)  # 接收者
        msg['Subject'] = Header('Test Feedback Email', 'utf-8')     # 邮件标题

        # 邮箱正文 ，三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        # message = MIMEText('Python sendmail test', 'plain', 'utf-8')
        mail_msg = MIMEText("""
        <p>Python 邮件发送图文</p>
        <p>测试截图：</p>
        <p><img  height="600" width="300" src="cid:image1"></p>
        <p><a href="http://www.baidu.com">这是一个链接</a></p>
        """, 'html', 'utf-8')       # cid 即Content-Id java或python发邮件时使用，在HTML格式的正文中可以使用这个唯一标识号来引用内嵌资源。
        msg.attach(mail_msg)

        # 指定图片的目录，读取图片
        file = open('test.png', 'rb')
        img_data = file.read()
        file.close()
        # 图片植入
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