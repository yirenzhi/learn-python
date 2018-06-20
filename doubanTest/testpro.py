import os
import time
import random
import requests
from contextlib import closing
def getProxiesUrl():
    proxies=[]
    with open('proxies.txt', 'r') as f:
        ips = f.readlines()
        for ip in ips:
            ip = 'http:\\' +ip.strip('\n')
            pro = {'proxy':ip}
            proxies.append(pro)
    return proxies
proxies = getProxiesUrl()

# while True:
#     print(random.choice(proxies))
#     time.sleep(1)


def download_mp4(url,dir):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name','Referer':'http://91porn.com'}
    req=requests.get(url=url)
    print(req.status_code)
    filename=str(dir)+'/1.mp4'
    with open(filename,'wb') as f:
        f.write(req.content)

def download_mp41(url,dir):
    # headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name','Referer':'http://91porn.com'}
    # req=requests.get(url=url)
    # filename=str(dir)+'/1.mp4'
    # with open(filename,'wb') as f:
    #     f.write(req.content)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name','Referer':'http://91porn.com'}
    filename=str(dir)+'/2.mp4'
    with closing(requests.get(url, stream=True ,headers=headers)) as response:
        chunk_size = 1024*1024
        content_size = int(response.headers['content-length'])
        print(response.status_code)
        assert response.status_code == 200
        with open(filename, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)

murl ='https://v.vzuu.com/video/963438899410026496'
# 'http://185.38.13.159//mp43/102331.mp4?st=dqRdugMUZcb3G4_NRAOZlw&e=1520484728'
# 'http://91porn.com/view_video.php?viewkey=500de3cb1cc0d0391e78&page=1&viewtype=basic&category=mf'
# 'http://185.38.13.130//mp43/37669.mp4?st=I_smnK1Fm0su1v8f6ARsbA&e=1520491340'
# http://185.38.13.159//mp43/102331.mp4?st=dqRdugMUZcb3G4_NRAOZlw&e=1520484728


download_mp41(murl,'.')
