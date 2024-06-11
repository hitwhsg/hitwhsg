import scrapy
import re
#import BaseSpider
import sys
sys.path.append('/home/shige/sg/sg')
from sg.items import SgItem
#import Selector
from scrapy.selector import Selector



class NewsSpider(scrapy.Spider):
    name = "news"
    test = "test"
    # allowed_domains = ["http://news.hitwh.edu.cn/"]
    start_urls = ['http://news.hitwh.edu.cn/']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                new = re.findall(r"[i][d][=]\d{5}", href)[0]
                url = 'http://news.hitwh.edu.cn/news_detail.asp?' + new
                yield scrapy.Request(url, callback=self.parse_news)
            except:
                continue
    def parse_news(self, response):
        sel = Selector(response)
        item = SgItem()
        item['url'] = response.url
        item['title'] = sel.xpath("//div[@id='newsTitle']").extract()
        item['body'] = sel.xpath("//div[@id='newsContnet']//p//text()").extract()
        return item
