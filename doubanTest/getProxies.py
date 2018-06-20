# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用

from bs4 import BeautifulSoup
import requests
import random

def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

def saveProxies(ip_list):
    for url in ip_list:
        ceshiUrl = "https://www.baidu.com"
        pro = {'proxy':'http:\\' +url}
        try :
            s = requests.get(ceshiUrl,proxies = pro)
            print (s.status_code)
            if s.status_code==200:
                with open('proxies.txt', 'a+') as f:
                    f.write(url+'\n')
        except Exception as e:
            print (e)



if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    ip_list = get_ip_list(url, headers=headers)
    saveProxies(ip_list)
