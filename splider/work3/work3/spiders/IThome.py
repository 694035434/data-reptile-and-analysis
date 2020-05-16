# -*- coding: utf-8 -*-
import scrapy
import re
from work3.items import Work3Item
class IthomeSpider(scrapy.Spider):
    name = 'IThome'
    allowed_domains = ['www.ithome.com']
    start_urls = []
    for i in range(1,11):
        url='https://www.ithome.com/list/list_'+str(i)+'.html'
        start_urls.append(url)


    def parse(self, response):
        item=Work3Item()
        it_class=response.xpath('//*[@id="wrapper"]/div[1]/div/ul/li/strong/a/text()').extract()
        it_title=response.xpath('//*[@id="wrapper"]/div[1]/div/ul/li/a/text()').extract()
        it_time=response.xpath('//*[@id="wrapper"]/div[1]/div/ul/li/span/text()').extract()
        title=[]
        for i in range(len(it_class)):
            title.append(re.sub("\s","",it_title[i]))
        item["it_class"]=it_class
        item["it_title"]=title
        item["it_time"]=it_time

        yield item

