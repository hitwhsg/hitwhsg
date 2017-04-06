# -*- coding: utf-8 -*-
import scrapy
import re
import BaseSpider
import SgItem
import Selector


class NewsSpider(scrapy.Spider):
    name = "news"
    #allowed_domains = ["http://news.hitwh.edu.cn/"]
    start_urls = ['http://news.hitwh.edu.cn/']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                new = re.findall(r"[i][d][=]\d{5}",href)[0]
                url = 'http://news.hitwh.edu.cn/'+ new
                yield scrapy.Request(url, callback=self.parse_news)
	    except:
	        continue
            
    def parse_news(self,response):
        sel = Selector(response)
        sg = SgItem()  
        sg['url'] = response.url  
        sg['title'] = sel.xpath("//div[@id='newsTitle']").extract()  
        sg['body'] = sel.xpath("//div[@id='content']//p//text()").extract()  
        return sg  
