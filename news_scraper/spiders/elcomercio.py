# -*- coding: utf-8 -*-
import scrapy

from news_scraper.items import NewItem

class ElComercioSpider(scrapy.Spider):
    name = "elcomercio"
    allowed_domains = ["elcomercio.pe"]
    start_urls = ['http://www.elcomercio.pe/archivo/2016-05-08']

    def parse(self, response):
        for new in response.css(".f-detalle"):
            item = NewItem()
            item['title'] = new.css("h2 a::text").extract()
            yield item
