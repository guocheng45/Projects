import smtplib
from email.mime.text import MIMEText
from email.header import Header


def test_sendMail():
    # ����������¼������Ϳ���
    password = 'sdjxhqksmlfsbghd'  # ������Ȩ��
    smtp_server = 'smtp.qq.com'  # ���ŷ�����

    sender = '467563369@qq.com'
    receivers = '467563369@qq.com'  # ['467563369@qq.com','a1804536661@qq.com']        # ��������

    # �������� ��������������һ��Ϊ�ı����ݣ��ڶ��� plain �����ı���ʽ�������� utf-8 ���ñ���
    message = MIMEText('Python sendmail test', 'plain', 'utf-8')

    # �ʼ�ͷ��Ϣ
    message['From'] = Header('Test_sender', 'utf-8')  # ������
    message['To'] = Header('receivers', 'utf-8')  # ������
    message['Subject'] = Header('Python Email Subject', 'utf-8')
    # 1234 shanchu

    try:
        # �������ŷ�������ʹ�õ��Ǽ��ܴ���
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(smtp_server, 465)
        smtpObj.login(sender,password)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("send mail success")
    except smtplib.SMTPException:
        print("Error: can not send the mail")
    finally:
        # �رշ�����
        smtpObj.quit()

