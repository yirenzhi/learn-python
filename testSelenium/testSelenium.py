#爬取知乎图片
#通过selenium模拟网页的滚动获取所有图片并爬取
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import tools
import re
def start1():
    cap = webdriver.DesiredCapabilities.PHANTOMJS
    cap["phantomjs.page.settings.resourceTimeout"] = 180
    cap["phantomjs.page.settings.loadImages"] = False

    driver = webdriver.PhantomJS(executable_path="D:\\Downloads\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe", desired_capabilities=cap)
    driver.set_page_load_timeout(180)     
    driver.get('https://www.zhihu.com/question/26297181?utm_source=qq&utm_medium=social&utm_oi=924791125112406016')
    time.sleep(5)
    driver.save_screenshot('./login.png')   #为便于调试，保存网页的截图

#获取所有图片，然后调用getPic爬取所有图片
def start():
    cap = webdriver.DesiredCapabilities.CHROME
    cap["chrome.page.settings.resourceTimeout"] = 180
    cap["chrome.page.settings.loadImages"] = False
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", desired_capabilities=cap)
    driver.set_page_load_timeout(180)
    driver.get("https://www.zhihu.com/question/26297181?utm_source=qq&utm_medium=social&utm_oi=924791125112406016")
    # time.sleep(5)
    assert '知乎' in driver.title
    print(driver.title)
    scrollPage(driver)
    with open('test1.html','w',encoding='utf-8') as th:
        th.write(driver.page_source)

    driver.quit()
    

def scrollPage(driver1):
    t1 = time.time()
    n=100
    for i in range(1,n):
        # s = "window.scrollTo(0,document.body.scrollHeight/{0}*{1});".format(n,i)
        s = "window.scrollTo(0,document.body.scrollHeight);"
        print(s,len(driver1.page_source),time.time()-t1)
        driver1.execute_script(s)
        
def test1():
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.get('http://www.baidu.com')

    elem = driver.find_element_by_name('wd')
    elem.send_keys("python")
    elem.send_keys(Keys.RETURN)
    time.sleep(5)

def getPic():
    with open('test1.html','r',encoding='utf-8') as fp:
        dbcontent=fp.read()
        soup = BeautifulSoup(dbcontent,'html.parser')
        list1 = soup.find_all('div',class_="List-item")
        print('用户总量：'+str(len(list1)))
        listName = []
        i = 0
        nums =0
        for temp in list1:
            name = temp.find('span', class_='UserLink AuthorInfo-name')
            if not name:
                continue
            nameStr = name.string
            while nameStr in listName:
                nameStr = nameStr+str(i)
                i+=1
            listName.append(nameStr)
            print(nameStr)
            imgs = temp.find_all('img')
            listUrl = []
            for img in imgs:
                print(img['src'])
                listUrl.append(img['src'])
            #传递name和图片地址list,创建文件夹下载图片
            if len(listUrl)>1:
                nums+=1
                print("下载第%d位用户。"% nums)
                createDir(nameStr,listUrl)


def createDir(name, urls):
    basicPath = './pic4/'
    path = basicPath+name+'/'
    tools.mkdir(path)

    #下载图片
    for url in urls:
        print(url)
        re1 = re.search( r'.{8}\.jpg', url)
        if re1:
            name = re1.group().replace('_','')
            pathPic = path+name
            print('图片保存在：'+pathPic)
            tools.downPic(url,pathPic)

getPic()