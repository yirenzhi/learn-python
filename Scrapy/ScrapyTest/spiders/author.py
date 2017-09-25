import scrapy
from ScrapyTest.items import AuthorItem

class AuthorSpider(scrapy.Spider):
    name='author'

    start_urls =['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
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
