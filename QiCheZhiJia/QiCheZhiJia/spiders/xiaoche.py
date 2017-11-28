import scrapy
from ScrapyTest.items import AuthorItem

class AuthorSpider(scrapy.Spider):
    name='xiaoche'

    start_urls =['http://www.autohome.com.cn/a0/#pvareaid=103177']

    def parse(self, response):

        bb=response.css('ul[class=rank-list-ul] h4 a::attr(href)').extract()
        #因为有列表和图片两种模式所以数量要除以2
        cars_urls=bb[:length(bb)/2]
        #http://car.autohome.com.cn/config/series/81.html

        for url in cars_urls:
            peizhi_url = 'http://car.autohome.com.cn/config/series/'+url.split('/')[3]+'.html'
            yield response.follow(peizhi_url,callback=self.parseAuthor)

        for a in response.css('.author + a::attr(href)'):
            yield response.follow(a,callback=self.parseAuthor)

        for a in response.css('li.next a'):
            yield response.follow(a,callback=self.parse)



    def parseAuthor(self,response):
        authorItem = AuthorItem()
        authorItem['name']=response.css('h3.author-title::text').extract_first().strip(),
        authorItem['bir']=response.css('span.author-born-date::text').extract_first().strip(),
        #authorItem['bio']=response.css('div.author-description::text').extract_first()[:30].strip(),

        yield authorItem
        #print response.css('h3.author-title').extract_first()


    def parsePeiZhi(self,response):
        response.css('ul[class=rank-list-ul] h4 a::text').extract()
