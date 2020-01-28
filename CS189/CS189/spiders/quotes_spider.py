import scrapy
from ..items import Cs189Item

class QuoteSpider(scrapy.Spider):

    name = 'project189'
    url = input("ULR: ")
    start_urls = [url]
    #https://blog.hubspot.com/marketing/beginner-blogger-mistakes

    def parse(self, response):

        items = Cs189Item()

        title = response.css('title::text').extract()
        items['title'] = title

        items['paragraph'] = response.css('#hs_cos_wrapper_post_body p::text').extract()

        yield items
