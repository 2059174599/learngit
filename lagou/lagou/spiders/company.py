# -*- coding: utf-8 -*-
from lagou.items import LagouItem
import scrapy


class CompanySpider(scrapy.Spider):
	name = 'company'
	allowed_domains = ['lagou.com/gongsi/']
	start_urls = ['http://lagou.com/gongsi/']
	item = LagouItem()
	def parse(self, response):
		item = LagouItem()
		tag_url = response.xpath('//li[@class="wrapper"]//div/ul/li/a/@href')
		next_page = response.xpath('//div[@class="pager_container"]/span[last()]/@class')
		for each in response.xpath('//li[@class="company-item"]'):
			lg_company_url = each.xpath('div/p[1]/a/@href').extract_first()
			tag = each.xpath('div/p[@class="indus-stage wordCut"]/text()').extract_first()
			item['tag'] = tag
			item['lg_company_url'] = lg_company_url
			# for i in range(1,21):


			#print(item,next_page)
		# for url in tag_url:
		# 	yield scrapy.Request(next_page, callback=self.parse)
			print(lg_company_url)
			yield scrapy.Request(lg_company_url,callback=self.company_page)
	def company_page(self,response):
		print('开始回调')
		# item = LagouItem()
		# company_url = response.xpath('//H1/a/@href').extract_first()
		# company_word = response.xpath('//div[@class="company_word"]').extract_first()
		# item['company_url'] = company_url
		# item['company_word'] = company_word
		# print(item)