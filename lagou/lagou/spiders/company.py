# -*- coding: utf-8 -*-
from lagou.items import LagouItem
import scrapy


class CompanySpider(scrapy.Spider):
    name = 'company'
    allowed_domains = ['lagou.com/gongsi/']
    start_urls = ['http://lagou.com/gongsi/']

    def parse(self, response):
        for each in response.xpath('//div[@class="item_con_list"]'):
	        item = LagouItem()
	        name = each.xpath('p[@class="indus-stage wordCut"]/text()')
	    	company_url = each.xpath('p[@class="company-name wordCut"]/a/text()')
	        item['label'] = name[0]
	        item['company_url'] = company_url[0]
	        ptint(item)