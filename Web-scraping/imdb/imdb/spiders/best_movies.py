# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//td[@class='titleColumn']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield{
        "Title": response.xpath("//div[@class='title_wrapper']/h1/text()").get().strip(),
        "director": response.xpath("//div[@class='credit_summary_item']/a/text()").get().strip(),
        "mpa_rating": response.xpath("//div[@class='subtext']/text()").get().strip(),
        "length": response.xpath("//time/text()").get().strip(),
        "genre": response.xpath("//div[@class='subtext']/a/text()").get().strip(),
        "release_date": response.xpath("//a[@title='See more release dates']/text()").get().strip(),
        "imdb_rating": response.xpath("//span[@itemprop='ratingValue']/text()").get().strip(),
        "vote_count": response.xpath("//span[@itemprop='ratingCount']/text()").get().strip(),
        "synopsis": response.xpath("//div[@class='summary_text']/text()").get().strip(),
        }
