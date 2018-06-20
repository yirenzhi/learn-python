import smtplib
from email.mime.text import MIMEText
from email.header import Header

def SendEmail(fromAdd, toAdd, subject, attachfile, htmlText):
  strFrom = fromAdd;
  strTo = toAdd;
  msg =MIMEText(htmlText);
  msg['Content-Type'] = 'Text/HTML';
  msg['Subject'] = Header(subject,'gb2312');
  msg['To'] = strTo;
  msg['From'] = strFrom;

  _user = '328478762@qq.com'
  _pwd = '授权码'
  smtp = smtplib.SMTP('smtp.qq.com');
  smtp.login(_user,_pwd);
  try:
    smtp.sendmail(strFrom,strTo,msg.as_string());
  finally:
    smtp.close;

if __name__ == "__main__":
  SendEmail("328478762@qq.com","328478762@qq.com","","hello","hello world");

# import smtplib
# from email.mime.text import MIMEText
# _user = "你的qq邮箱"
# _pwd  = "你的授权码"
# _to   = "501257367@163.com"
#
# msg = MIMEText("Test")
# msg["Subject"] = "don't panic"
# msg["From"]    = _user
# msg["To"]      = _to
#
# try:
#     s = smtplib.SMTP_SSL("smtp.qq.com", 465)
#     s.login(_user, _pwd)
#     s.sendmail(_user, _to, msg.as_string())
#     s.quit()
#     print "Success!"
# except smtplib.SMTPException,e:
#     print "Falied,%s"%e
