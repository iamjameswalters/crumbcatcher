import scrapy


class CrumblSpider(scrapy.Spider):
    name = "crumbl"
    allowed_domains = ["crumblcookies.com"]
    start_urls = ["https://crumblcookies.com"]

    def parse(self, response):
        
        pass
