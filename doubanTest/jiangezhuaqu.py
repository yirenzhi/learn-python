import requests
from bs4 import BeautifulSoup
import re
import os
import time
import testRequest
#每隔一分钟，抓取下首页图片

titlesList=[]
picCount=1
def Bsjiexi(dbcontent):
    #获取连接地址列表
    soup = BeautifulSoup(dbcontent,'html.parser')
    titles =soup.find_all('td',class_='td-subject')
    urls = []
    for temp in titles:
        tds = temp.select('~ td')
        if len(tds)>2:
            title = temp.a['title']
            print(title)
            if title in titlesList:
                continue
            titlesList.append(title)
            print(temp.a['href'])
            urls.append(temp.a['href'])
    return urls

def start():
    global picCount
    doubanurl = 'https://www.douban.com/group/'
    path = 'E:\\projectTest\\doubanpics2\\topics'
    ismkSuccess = testRequest.mkdir(path)
    dbcontent = testRequest.getFromUrl(doubanurl)
    lianjies = Bsjiexi(dbcontent)
    for lianjie in lianjies:
        time.sleep(2)
        dangeyemian = testRequest.getFromUrl(lianjie)
        pics = testRequest.jiexidange(dangeyemian)
        for pic in pics:
            print(pic)
            re1 = re.search( r'p\d+-*\d+\.jpg', pic)
            if re1:
                string = path+'\\'+re1.group()
                print('图片下载地址：'+string)
                testRequest.downPic(pic,string)
                print('第'+str(picCount)+'张图片下载完成')
                time.sleep(1)
                picCount+=1

if __name__== '__main__':
    while True:
        start()
        print('*'*50)
        print('休息30秒')
        time.sleep(30)
