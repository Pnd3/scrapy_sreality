import scrapy
import json

from srealitycraper.items import SrealitycraperItem 


class SrealitySpider(scrapy.Spider):
    name = "sreality"
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500&page=0']

    def parse(self, response):
        flats = json.loads(response.body)
        for flat in flats['_embedded']['estates']:
            title = flat['name'].replace('\s', '')
            image_url = flat['_links']['images'][0]['href']

            item = SrealitycraperItem()
            item['title'] = title
            item['image_url'] = image_url

            yield item