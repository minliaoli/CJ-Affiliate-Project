import scrapy
from CS189.CS189.items import Cs189Item
from scrapy.crawler import CrawlerProcess
import json


class MySpider(scrapy.Spider):

    name = 'project189'

    def parse(self, response):

        items = Cs189Item()

        title = response.css('title::text').extract()
        paragraph = response.css('#hs_cos_wrapper_post_body p::text').extract()

        items['title'] = title
        items['paragraph'] = paragraph
        yield items


def run(url):

    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json'
    })
    process.crawl(MySpider, start_urls=[url])
    process.start()  # the script will block here until the crawling is finished

    return read_json()


def read_json():
    with open("output.json",'r') as f:
        data = json.load(f)
    f.close()

    return data

'''
if __name__ == '__main__':

    url = 'https://blog.hubspot.com/marketing/beginner-blogger-mistakes'

    print(run(url))
'''



