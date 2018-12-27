# -*- coding: utf-8 -*-
from lagou.items import LagouItem
import scrapy


class CompanySpider(scrapy.Spider):
	name = 'company'
	allowed_domains = ['lagou.com/gongsi/']
	start_urls = ['http://lagou.com/gongsi/']

	def parse(self, response):
		# for each in response.xpath('//div[@class="item_con_list"]'):
		tag_url = response.xpath('//li[@class="wrapper"]//li/a/@href').extract()
		title = response.xpath('//h1/text()')
		item = LagouItem()
	 #        #name = each.xpath('p[@class="indus-stage wordCut"]/text()')
	 #    	#company_url = each.xpath('p[@class="company-name wordCut"]/a/text()')
		item['label'] = title
		item['company_url'] = 'wl'
		next_page = response.xpath('//div[@class="pager_container"]/span[last()]/@class')
		print(item,tag_url,next_page)
		# for url in tag_url:
		# 	yield scrapy.Request(next_page, callback=self.parse)

		yield item