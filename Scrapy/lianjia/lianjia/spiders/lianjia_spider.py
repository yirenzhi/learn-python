# -*- coding=utf-8 -*-

import scrapy,csv,sys
from lianjia.items import LianjiaItem
reload(sys)
sys.setdefaultencoding('utf8')
class AuthorSpider(scrapy.Spider):
    name='lianjia'

    start_urls =['http://sh.lianjia.com/ditiezufang/li143685066s100022067/l2']

    datas=[]
    def parse(self, response):
        for info in response.css('ul[id=house-lst] div[class=info-panel]'):
            #yield response.follow(info,callback=self.parseInfo)
            self.parseInfo(info)

        next_page = response.css('div.page-box.house-lst-page-box a[gahref=results_next_page]::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print("url:::::"+next_page)
            yield scrapy.Request(next_page, callback=self.parse)

        self.save_csv(self.datas)

    def parseInfo(self,info):
        lianjiaItem = LianjiaItem()
        lianjiaItem['subway'] = info.css('span.fang-subway-ex span::text').extract_first()
        lianjiaItem['title']=info.css('h2 a::text').extract_first();

        wheres = info.css('div.where span')
        lianjiaItem['xiaoqu']=wheres[0].css('::text').extract_first()
        lianjiaItem['huxing']=wheres[1].css('::text').extract_first()
        lianjiaItem['area']=wheres[2].css('::text').extract_first()
        lianjiaItem['price'] = info.css('div.price span.num::text').extract_first()
        lianjiaItem['release_time'] = info.css('div.price-pre::text').extract_first()[:10]
        lianjiaItem['crawling_time'] = ''
        lianjiaItem['url'] = 'http://sh.lianjia.com'+info.css('h2 a::attr(href)').extract_first()
        data=[lianjiaItem['subway'],lianjiaItem['title'],lianjiaItem['xiaoqu'],lianjiaItem['huxing'],lianjiaItem['area'],lianjiaItem['price'],lianjiaItem['release_time'],lianjiaItem['crawling_time'],lianjiaItem['url']]
        self.datas.append(data)



    def save_csv(self,datas):
        with open('lianjia.csv','w+') as csvfile:
            #地铁 标题 小区 户型 面积 价格 发布时间 爬取时间 链接url
            fieldnames=['地铁',' 标题 ','小区',' 户型',' 面积 ','价格 ','发布时间 ','爬取时间 ','链接url']
            #writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
            #writer.writeheader()
            writer = csv.writer(csvfile,dialect='excel')
            writer.writerow(fieldnames)
            for data in datas:
                writer.writerow(data)
