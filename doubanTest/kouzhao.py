import requests
'''
name: 周达
mobilePhone: 17521220929
idCard: 340221199310151595
shopId: 982

Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 84
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: JSESSIONID=ab7bf85b-b7b6-4c18-a031-0d5581e3b42c
Host: kz.ahsyy.com:8099
Origin: http://kz.ahsyy.com:8099
Referer: http://kz.ahsyy.com:8099/register
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
X-Requested-With: XMLHttpRequest
'''
header_data={'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    'Host':'kz.ahsyy.com:8099',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36X-Requested-With: XMLHttpRequest',

    }
login_data = {'name':'周达','mobilePhone':'17521220929','idCard':'340221199310151595','shopId':'982'}
r=requests.post('http://kz.ahsyy.com:8099/register',data=login_data,headers=header_data,verify=True)
print(r.content)