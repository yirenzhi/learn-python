#coding : UTF-8
import requests,csv
from bs4 import BeautifulSoup

def get_content(url, data = None):
    r = requests.get(url)
    r.encoding = 'utf-8'
    print(r.status_code)
    return r.text
    
    '''
    #网页保存到本地
    file_obj = open("test.txt","w")
    file_obj.write(r.text)
    file_obj.close()
    '''

def get_data(html_text):
    data=[]
    bs=BeautifulSoup(html_text,'html.parser')
    body = bs.body
    div = body.find('div',{'id':'7d'})
    ul = div.find('ul')
    li = ul.find_all('li')
    for day in li:
        temp=[]
        #剥离出想要的四个元素
        days = day.find('h1').string
        wea = day.find('p',{'class':'wea'}).string
        tem = day.find('p',{'class':'tem'})
        #最高温度可能没有，取不到就填无
        try:
            max_tem = tem.find('span').string
        except:
            max_tem = '无'
        
        #print(max_tem)
        min_tem = tem.find('i').string
        win = day.find('p',{'class':'win'})
        fengli = win.find('i').string
        temp=[days,wea,max_tem,min_tem,fengli]
        data.append(temp)
    return data

def save_csv(data):
    with open('weather.csv','w',newline='') as csvfile:
        fieldnames=['日期','天气','最高温度','最低温度','风力']
        #writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        #writer.writeheader()
        writer = csv.writer(csvfile,dialect='excel')
        writer.writerow(fieldnames)
        for day in data:
            #writer.writerow({'日期':day[0],'天气':day[1],'最高温度':day[2],'最低温度':day[3],'风力':day[4]})
            writer.writerow(day)
            

    
if __name__== '__main__':
    url = 'http://www.weather.com.cn/weather/101020100.shtml'
    html=get_content(url)
    data=get_data(html)
    save_csv(data)
    print (data)

