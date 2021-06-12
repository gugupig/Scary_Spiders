# -*- coding: utf-8 -*-
import scrapy


class CreepycrwalerSpider(scrapy.Spider):
    name = 'creepycrwaler'
    allowed_domains = ['www.creepypasta.com']
    #start_urls = ['http://www.creepypasta.com/archive/top-ranked/#content/']
    
    def start_requests(self):
        yield scrapy.Request(url ='https://www.creepypasta.com/archive/top-ranked/#content' , callback = self.parse)
                            
        
        
    def parse(self, response):
        articles = response.xpath("//h2[@class ='pt-cv-title']/a")
        for res in articles:
            link = res.xpath("./@href").get()
            #name = res.xpath("./text()").get()
            yield response.follow(url = link,callback = self.parse_a)
        next_page = response.xpath('//a[text()="›"]')
        if next_page:
            yield  scrapy.Request(url = response.xpath('//a[text()="›"]/@href').get(),callback = self.parse)

    def parse_a (self,response):
        title = response.xpath("//h1[@class= 'entry-title']/text()").get()
        #rating = response.xpath("(//div[@class= 'gdrts-rating-text']/strong)[1]/text()").get()
        content = " ".join(response.xpath("//div[@class='entry-content clear']/p/text()").getall())
        #content = response.xpath("//div[@class='entry-content clear']/p/text()").getall()
        yield {"title": title,"content":content}        
