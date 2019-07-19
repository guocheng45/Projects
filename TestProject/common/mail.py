# -*- coding: utf-8-*-
"""发送邮件封装"""
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from common.fileReader import IniUtil
from socket import gaierror, error
from common.log import Log


# ===========================发送邮件==============================================
def send_report(file_new, to_addr, subject=u'接口自动化测试报告'):

    with open(file_new, 'rb') as f:
        mail_body = f.read()

    # to_addr = IniUtil().get_value_of_option('to_list', 'to_list_sup')
    to_lists = to_addr.strip(',').split(',')  # 这里需要是list类型
    smtp_server = IniUtil().get_value_of_option('mail', 'server')
    from_addr = IniUtil().get_value_of_option('mail', 'send_addr')
    password = IniUtil().get_value_of_option('mail', 'password')

    # 邮件对象
    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    # msg['From'] = from_addr
    msg['From'] = Header(u"FBBC自动化测试专用邮箱", 'utf-8')
    msg['To'] = ";".join(to_lists)  # 接收string，邮箱之间用分号；隔开
    print(msg['To'])
    # 邮件正文
    msg.attach(MIMEText(mail_body, 'html', 'utf-8'))

    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename= "test_report.html"'
    msg.attach(att)

    try:
        smtp = smtplib.SMTP(smtp_server, 25)  # 链接server
        # smtp.starttls()
    except (gaierror and error) as e:
        Log().error(u'发送邮件失败，无法链接到SMTP服务器，检查网络以及SMTP服务器. %s' % e)
    else:
        try:
            smtp.login(from_addr, password)  # 登陆邮箱
        except smtplib.SMTPAuthenticationError as e:
            Log().error('用户名密码验证失败！ %s' % e)
        else:
            smtp.sendmail(from_addr, to_lists, msg.as_string())
            Log().info(u'邮件发送成功！若没收到邮件，请检查垃圾箱，同时检查收件人地址是否正确')
        finally:
            smtp.quit()  # 断开链接


# ===============查找测试报告目录，找到最新生成的测试报告文件==============
# 参数为测试报告所在的路径
def new_report(report_path):
        # 返回测试报告所在目录下的所有文件列表
        report_list = os.listdir(report_path)

        # 获取按升序排序后的测试报告列表
        new_list = sorted(report_list)

        # 获取最后一个即最新的测试报告地址
        report = os.path.join(report_path, new_list[-1])
        return report


if __name__ == '__main__':
    f  = new_report(r'D:\SVN自动化\B2B_Interface\report')
    send_report(f)


