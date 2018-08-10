import requests

def getImg(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}
    r = requests.get(url, headers = headers)
    with open('test1.html','w',encoding='utf-8') as th:
        th.write(r.text)
url='https://www.zhihu.com/api/v4/questions/21624445/answers?&limit=5&offset=0&sort_by=default%20HTTP/1.1'
url='https://www.zhihu.com/question/28483870'
getImg(url)