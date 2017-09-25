# -*- coding: utf-8 -*-
import smtplib

sender = 'yiren_zhi@163.com'
receivers = ['32878762@qq.com']

message='''
from yiren_zhi@163.com to 328478762@qq.com
subject : smtp e-mail test
this is a test e-mail message.
'''

# try:
# smtpObj = smtplib.SMTP('localhost')
print('1')
smtpObj = smtplib.SMTP('smtp.qq.com')
print('2')
smtpObj.set_debuglevel(1)
print('3')
smtpObj.sendmail(sender, receivers, message)
print ("Successfully sent email")
# except SMTPException:
#     print ("Error: unable to send email")
