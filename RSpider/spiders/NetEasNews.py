# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from RSpider.items import NeteasynewsItem


class NeteasnewsSpider(CrawlSpider):
    name = 'NetEasNews'
    allowed_domains = ['news.163.com']
    start_urls = ['http://news.163.com/']

    rules = (
        Rule(LinkExtractor(allow=r'\d{2}/\d{4}/\d{2}/\w+\.html'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = NeteasynewsItem()

        i['title'] = response.xpath('//h1[@id="h1title"]/text()').extract()
        i['url'] = response.url
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
