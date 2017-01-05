#coding : UTF-8

from bs4 import BeautifulSoup
import requests


def get_content(url, data = None):
    r = requests.get(url)
    r.encoding = 'utf-8'
    print(r.status_code)

    '''
    #网页保存到本地
    file_obj = open("test.txt","w")
    file_obj.write(r.text)
    file_obj.close()
    #'''
    return r.text

def get_data(html_text):
    data=[]
    bs=BeautifulSoup(html_text,'html.parser')
    body = bs.body
    divs = body.find_all('div',{'class':'highlight'})
    #print (div)
    codes = ''
    for div in divs:       
        spans = div.find_all('span')
        for span in spans:          
            p=span.string
            if((r';' in p)or(r'//' in p)or(r'}' in p)or(r'{' in p)):
                p+='\n'
                if('{' in p):
                    p='\n'+p+'\t'
                if(';' in p):
                    p= p+'\t'
                if('//' in p):
                    p= p+'\t'
                
            codes+=p
        codes+='\n\n\n\n\n'
    return codes

def sava_files(data):
    file_obj = open("codes.txt","w")
    file_obj.write(data)
    file_obj.close()

if __name__== '__main__':
    url = 'http://www.360doc.com/content/13/0601/12/110467_289667212.shtml'
    html=get_content(url)
    codes = get_data(html)
    sava_files(codes)
