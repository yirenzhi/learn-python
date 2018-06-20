import requests
from bs4 import BeautifulSoup
import re
import os
import time
import random
# r = requests.get('https://www.douban.com/group/544865/?type=essence#topics')
#
# print(r.url)
# print(r.text)
# print(r.encoding)
# payload = {'key1':'value1','key2':'value2'}
#
# r1=requests.get("http://httpbin.org/get",params=payload)
# print(r1.url)
picCount=1
pageTag=0
basicPath = 'E:\\projectTest\\doubanpics6\\'
pathTag = 'lanjitopic'
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

def random_ip():
    a=random.randint(1,255)
    b=random.randint(1,255)
    c=random.randint(1,255)
    d=random.randint(1,255)
    return(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))
def getFromUrl(url):
    kwargs = {
            "headers": {
                "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                "Referer": "http://www.douban.com/",
                'X-Forwarded-For':random_ip(),
                'cookie' : '''ll="108296"; bid=-QdP6H0hcTQ; __yadk_uid=pWgi7AkfGFoStjoUxsCnlEBYaQ7PLI0K; gr_user_id=8a504e05-085b-46c2-9d28-516c044f680c; viewed="26163454_6025284_2112672_3004255"; _vwo_uuid_v2=D64180DB5D86354CBF26F3001AAD9B8BF|7ec05da5cc203951b65748930f0427aa; _ga=GA1.2.201063266.1517987979; __utmv=30149280.17060; __utmz=30149280.1528706800.47.20.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=30149280.201063266.1517987979.1528706800.1528855975.48; __utmc=30149280; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1528855989%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DeO6URpMpwOkTdtr2X4ds5w8YBKcHxbyZB4XwNlNdGSCUS-dyBEOmquwCtx7oSTDP%26ck%3D5362.5.87.142.155.152.232.348%26shh%3Dwww.baidu.com%26sht%3Dbaidu%26wd%3D%26eqid%3D8a6e75b30004b48c000000045b207dac%22%5D; _pk_ses.100001.8cb4=*; ps=y; dbcl2="170608811:agRGmQbo3zI"; ck=wlb8; push_noty_num=0; push_doumail_num=0; _pk_id.100001.8cb4=bf07b4ce34752813.1517987978.46.1528856559.1528706800.; __utmb=30149280.86.5.1528856559453''',
            },
        }

    cookiestr = '''ll="108296"; bid=-QdP6H0hcTQ; __yadk_uid=pWgi7AkfGFoStjoUxsCnlEBYaQ7PLI0K; gr_user_id=8a504e05-085b-46c2-9d28-516c044f680c; viewed="26163454_6025284_2112672_3004255"; _vwo_uuid_v2=D64180DB5D86354CBF26F3001AAD9B8BF|7ec05da5cc203951b65748930f0427aa; _ga=GA1.2.201063266.1517987979; __utmv=30149280.17060; __utmz=30149280.1528706800.47.20.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=30149280.201063266.1517987979.1528706800.1528855975.48; __utmc=30149280; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1528855989%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DeO6URpMpwOkTdtr2X4ds5w8YBKcHxbyZB4XwNlNdGSCUS-dyBEOmquwCtx7oSTDP%26ck%3D5362.5.87.142.155.152.232.348%26shh%3Dwww.baidu.com%26sht%3Dbaidu%26wd%3D%26eqid%3D8a6e75b30004b48c000000045b207dac%22%5D; _pk_ses.100001.8cb4=*; ps=y; dbcl2="170608811:agRGmQbo3zI"; ck=wlb8; push_noty_num=0; push_doumail_num=0; _pk_id.100001.8cb4=bf07b4ce34752813.1517987978.46.1528856559.1528706800.; __utmb=30149280.86.5.1528856559453'''
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36','X-Forwarded-For':random_ip()}
    cookies = {'cookie': cookiestr}
    # r = requests.get(url, cookies = cookies, headers = headers,proxies=random.choice(proxys))
    r = requests.get(url, headers = headers)
    # r = requests.get(url, headers = headers)
    return r.content
    # with open('douban_2.txt', 'wb+') as f:
    #     f.write(r.content)

def Bsjiexi(dbcontent):
    #获取连接地址列表
    soup = BeautifulSoup(dbcontent,'html.parser')
    titles =soup.find_all('td',class_='title')
    urls = []
    for temp in titles:
        tds = temp.select('~ td')
        if len(tds)>2:
            fanwenshu=tds[1].string
            if fanwenshu:
                if (int(fanwenshu)>2):
                    print(int(fanwenshu))
                    print(temp.a['title'])
                    print(temp.a['href'])
                    urls.append(temp.a['href'])

    return urls

def jiexidange(dbcontent):
    '''获取单个页面所有图片地址'''
    soup = BeautifulSoup(dbcontent,'html.parser')
    topics = soup.find_all('div',class_='topic-figure cc')
    topics1 = soup.find_all('div',class_='image-wrapper')
    pics = []
    for temp in topics:
        pics.append(temp.img['src'])
    for temp in topics1:
        pics.append(temp.img['src'])
    print(pics)
    return pics

#下载图片
def downPic(pic_url,path='pic'):
    if os.path.exists(pic_url):
        print('文件已存在！')
        return
    try:
        pic= requests.get(pic_url, timeout=10)
    except requests.exceptions.ConnectionError:
        print('【错误】当前图片无法下载')
    fp = open(path,'wb')
    fp.write(pic.content)
    fp.close()

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print (path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+' 目录已存在')
        return False

# doubanurl = 'https://www.douban.com/group/544865/?type=essence#topics'
# doubanurl = 'https://www.douban.com/group/jiatuizu/?type=essence#topics'
doubanurl = 'https://www.douban.com/group/516876/?type=essence#topics'

#获取一页列表的图片
def getOnePagePic(doubanurl):
    '''获取一页列表的图片地址,并返回下一页地址'''
    global pageTag
    global picCount
    dbcontent = getFromUrl(doubanurl)
    lianjies = Bsjiexi(dbcontent)
    path = basicPath+pathTag+'\\'
    for lianjie in lianjies:
        dangeyemian = getFromUrl(lianjie)
        pics = jiexidange(dangeyemian)
        for pic in pics:
            print(pic)
            re1 = re.search( r'p\d+-*\d+\.jpg', pic)
            if re1:
                string = path+'\\'+re1.group()
                print('图片保存在：'+string)
                downPic(pic,string)
                print('第'+str(picCount)+'张图片下载完成')
                sleepTimeS = random.randint(1,10)
                print('休息%d秒' % sleepTimeS)
                time.sleep(sleepTimeS)
                picCount+=1
    pageTag +=1
    if picCount>400:
        return
    soup = BeautifulSoup(dbcontent,'html.parser')
    #获取下一页标签，跳转下一页
    nextlist = soup.select('span.next a')
    return nextlist

def  recursionGetPic(firstUrl):
    '''从首页开始获取整页图片，然后递归的获取下一页'''
    if not firstUrl:
        return
    nextlist=getOnePagePic(firstUrl)
    if not nextlist:
        return
    if len(nextlist):
        nextUrl = nextlist[0]['href']
        print('*'*50)
        print('休息5秒')
        time.sleep(5)
        print('开始')
        print(nextUrl)
        recursionGetPic(nextUrl)




def start():
    global pathTag
    global picCount
    print('start+++++++++++++')
    # firstUrl = 'https://www.douban.com/group/521120/?type=essence#topics'
    # recursionGetPic(firstUrl)
    ziyuan = {'dapigu':'https://www.douban.com/group/544865/discussion?start=0',
                'jiatui':'https://www.douban.com/group/jiatuizu/discussion?start=0',
                'jiatuis':'https://www.douban.com/group/jiatuizu/discussion?start=500',
                'siwa':'https://www.douban.com/group/553239/discussion?start=0',
                'lanji':'https://www.douban.com/group/521120/discussion?start=0',
                'buzhengjin':'https://www.douban.com/group/bzjgirls/discussion?start=0',
    }
    newZiyuan = {
                # 'dapigu':'https://www.douban.com/group/544865/discussion?start=0',
                # 'jiatui':'https://www.douban.com/group/jiatuizu/discussion?start=0',
                # 'siwa':'https://www.douban.com/group/553239/discussion?start=0',
                'lanji':'https://www.douban.com/group/521120/discussion?start=0',
                'buzhengjin':'https://www.douban.com/group/bzjgirls/discussion?start=0',
                'daxiongfannao':'https://www.douban.com/group/338644/discussion?start=100',
                'daxiongmei':'https://www.douban.com/group/510760/discussion?start=0',
                'buyaohaixiu':'https://www.douban.com/group/606392/discussion?start=0',
                'buyaodaxiong':'https://www.douban.com/group/187765/discussion?start=0',
                'qiaoPP':'https://www.douban.com/group/qiaoPP/discussion?start=0',
                'XGzhaopian':'https://www.douban.com/group/DQMQQ/discussion?start=0',
                'haoxiongmmei':'https://www.douban.com/group/516876/discussion?start=0',
                'meixiong':'https://www.douban.com/group/32788/discussion?start=0',
                'dingziku':'https://www.douban.com/group/436738/discussion?start=0',
                'CTdaxiong':'https://www.douban.com/group/561425/discussion?start=0',
                'haixiuzu':'https://www.douban.com/group/haixiuzu/discussion?start=0',
                'dachangtui':'https://www.douban.com/group/meituikong/discussion?start=0',
                'chihewanle':'https://www.douban.com/group/beijing/discussion?start=0',
                'haoxiongmei':'https://www.douban.com/group/516876/discussion?start=0'

    }
    jixuZiyuan = {
                'haixiuzu':'https://www.douban.com/group/haixiuzu/discussion?start=0',
                'daxiongmei':'https://www.douban.com/group/510760/discussion?start=0',
                'dachangtui':'https://www.douban.com/group/meituikong/discussion?start=0',
                'chihewanle':'https://www.douban.com/group/beijing/discussion?start=0',
                'haoxiongmei':'https://www.douban.com/group/516876/discussion?start=0'
    }
    for key,value in newZiyuan.items():
        pathTag=key
        path = basicPath+pathTag+'\\'
        ismkSuccess = mkdir(path)
        recursionGetPic(value)
        str1=pathTag+'共下载'+str(picCount)+'张图片'
        print(str1)
        with open('douban_1.txt', 'a+') as f:
            f.write(str1+'\n')
        picCount=1

if __name__== '__main__':
    start()
