import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors  import LinkExtractor 

class AlletsySpider(scrapy.Spider):
    name = 'alletsy'
    allowed_domains = ['etsy.com']
    start_urls = ['http://etsy.com/']

    def parse(self, response):
        pass
