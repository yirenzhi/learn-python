'''
https://www.dbmeinv.com/dbgroup/rank.htm?pager_offset=1
豆瓣美女热门图片抓取，通过登陆后从浏览器复制cookies的方式获得权限
'''
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
basicPath = 'E:\\projectTest\\doubanmeinv\\'
pathTag = 'lanjitopic'
# def getProxiesUrl():
#     proxies=[]
#     with open('proxies.txt', 'r') as f:
#         ips = f.readlines()
#         for ip in ips:
#             ip = 'http:\\' +ip.strip('\n')
#             pro = {'proxy':ip}
#             proxies.append(pro)
#     return proxies
# proxies = getProxiesUrl()
def getFromUrl(url):
    kwargs = {
            "headers": {
                "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                "Referer": "http://www.douban.com/",
                'cookie' : '''ll="108296"; bid=-QdP6H0hcTQ; ps=y; ct=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1518328264%2C%22https%3A%2F%2Faccounts.douban.com%2Fsafety%2Funlock_sms%2Fresetpassword%3Fconfirmation%3D166561213372aead%26alias%3D%22%5D; __utmt=1; ap=1; _ga=GA1.2.201063266.1517987979; _gid=GA1.2.808929195.1518313530; dbcl2="170608811:BB1ByzScKT4"; ck=bv_C; _pk_id.100001.8cb4=bf07b4ce34752813.1517987978.24.1518328599.1518320796.; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utma=30149280.201063266.1517987979.1518319597.1518328266.24; __utmb=30149280.14.10.1518328266; __utmc=30149280; __utmz=30149280.1518328266.24.5.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/safety/unlock_sms/resetpassword; __utmv=30149280.17060''',
            },
        }

    cookiestr = '''ll="108296"; bid=-QdP6H0hcTQ; ps=y; ct=y; __yadk_uid=pWgi7AkfGFoStjoUxsCnlEBYaQ7PLI0K; _ga=GA1.2.201063266.1517987979; viewed="3004255"; _vwo_uuid_v2=D64180DB5D86354CBF26F3001AAD9B8BF|7ec05da5cc203951b65748930f0427aa; gr_user_id=8a504e05-085b-46c2-9d28-516c044f680c; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1520333152%2C%22https%3A%2F%2Fopen.weixin.qq.com%2Fconnect%2Fqrconnect%3Fappid%3Dwxd9c1c6bbd5d59980%26redirect_uri%3Dhttps%253A%252F%252Fwww.douban.com%252Faccounts%252Fconnect%252Fwechat%252Fcallback%26response_type%3Dcode%26scope%3Dsnsapi_login%26state%3D-QdP6H0hcTQ%252523None%252523https%25253A%252F%252Fwww.douban.com%252Fdoulist%252F2645411%252F%22%5D; ap=1; dbcl2="170608811:YPJKEO4ptL8"; ck=j2QD; _pk_id.100001.8cb4=bf07b4ce34752813.1517987978.33.1520333813.1520242238.; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utmt=1; __utma=30149280.201063266.1517987979.1520242006.1520333152.35; __utmb=30149280.88.5.1520333813446; __utmc=30149280; __utmz=30149280.1520242006.34.11.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.17060'''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    cookies = {'cookie': cookiestr}
    # r = requests.get(url, cookies = cookies, headers = headers,proxies=random.choice(proxys))
    # r = requests.get(url, headers = headers,proxies=random.choice(proxies))
    r = requests.get(url, headers = headers)
    return r.content
    # with open('douban_2.txt', 'wb+') as f:
    #     f.write(r.content)


def jiexidange(dbcontent):
    '''获取单个页面所有图片地址'''
    soup = BeautifulSoup(dbcontent,'html.parser')
    lis = soup.find_all('li',class_='span3')
    pics = []
    for temp in lis:
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
        return
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


#获取一页列表的图片
def getOnePagePic(doubanurl):
    '''获取一页列表的图片地址,并返回下一页地址'''
    global pageTag
    global picCount
    dbcontent = getFromUrl(doubanurl)

    pics = jiexidange(dbcontent)
    path = basicPath+pathTag+'\\'
    for pic in pics:
        print(pic)
        re1 = re.search( r'.{8}\.jpg', pic)
        if re1:
            string = path+'\\'+re1.group()
            print('图片保存在：'+string)
            downPic(pic,string)
            print('第'+str(picCount)+'张图片下载完成')
            picCount+=1
    pageTag +=1
    soup = BeautifulSoup(dbcontent,'html.parser')
    #获取下一页标签，跳转下一页
    nextlist = soup.select_one('a[title="下一页"]')['href']
    return nextlist

def  recursionGetPic(firstUrl):
    '''从首页开始获取整页图片，然后递归的获取下一页'''
    if not firstUrl:
        return
    nextUrl=getOnePagePic(firstUrl)
    if not nextUrl:
        return

    nextUrl = 'https://www.dbmeinv.com'+nextUrl
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
    remen={
        'remen621':'https://www.dbmeinv.com/dbgroup/rank.htm?pager_offset=979'
    }
    for key,value in remen.items():
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
