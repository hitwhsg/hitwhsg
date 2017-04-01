import scrapy
import re


class NewsSpider(scrapy.Spider):
    name = "news"
    #allowed_domains = ["http://news.hitwh.edu.cn/"]
    start_urls = ['http://news.hitwh.edu.cn/']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                new = re.findall(r"[i][d][=]\d{5}",href)[0]
                url = 'http://news.hitwh.edu.cn/'+ new
        pass
