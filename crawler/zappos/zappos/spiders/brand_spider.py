import scrapy


class TigerSpider(scrapy.Spider):
    name = 'brand'
    start_urls = ['https://www.zappos.com/b/onitsuka-tiger-by-asics/brand/421']

    def parse(self, response):
        shoes_link = response.css(
            'a.gae-click\*Brand-Landing-Page-Onitsuka-Tiger-by-Asics\*Category-Navigation\*Mens-Shoes::attr(href)')\
            .extract_first()
        yield response.follow(shoes_link, self.parse_condition)

    # sort products as desired
    def parse_condition(self, response):

        search_condition = response.css('span._1mDci div._3W23B div._1D58P div._1zlxc').xpath(
            './/a[@title="Sort by Price: Low to High"]/@href').extract_first()
        if search_condition is not None:
            yield response.follow(search_condition, self.parse_shoes)

    def parse_shoes(self, response):

        for resp in response.xpath('.//div[@id="searchPage"]').css('article._1h6Kf'):
            yield {
                'brand': resp.xpath('.//a/div[@class="_2jktc"]/p[@class="_1HOLv"]/span/text()').extract_first(),
                'name': resp.xpath('.//a/div[@class="_2jktc"]/p[@class="_3BAWv"]/text()').extract_first(),
                'price': resp.xpath('.//a/div[@class="_2jktc"]/p[@class="_1J1ab"]/span/text()').extract_first(),
            }
