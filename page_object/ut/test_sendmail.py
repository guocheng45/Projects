import smtplib
from email.mime.text import MIMEText
from email.header import Header

def test_sendMail():
    sender = '467563369@qq.com'
    password = 'sdjxhqksmlfsbghd'       # ������Ȩ��
    smtp_server = 'smtp.qq.com'         # ���ŷ�����

    receivers = '467563369@qq.com'#['467563369@qq.com','a1804536661@qq.com']        # ��������


    # �������� ��������������һ��Ϊ�ı����ݣ��ڶ��� plain �����ı���ʽ�������� utf-8 ���ñ���
    message = MIMEText('Python sendmail test','plain','utf-8')

    # �ʼ�ͷ��Ϣ
    message['From'] = Header('sender','utf-8')    # ������
    message['To'] = Header('receivers','utf-8')       # ������
    message['Subject'] = Header('Python Email Subject','utf-8')

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender,receivers,message.as_string())
        print("send mail success")
    except smtplib.SMTPException:
        print("Error: can not send the mail")
    # �ʼ�ͷ��Ϣ
    # message['From'] = Header(sender)
    # message['To'] = Header(receivers)
    # message['Subject'] = Header('python test')
    #
    # # �������ŷ�������ʹ�õ��Ǽ��ܴ���
    # server = smtplib.SMTP_SSL()
    # server.connect(smtp_server, 465)
    # # ��¼��������
    # server.login(sender, password)
    # # �����ʼ�
    # server.sendmail(sender, receivers, message.as_string())
    # # �رշ�����
    # server.quit()