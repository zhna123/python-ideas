import scrapy


class QuotesSpider(scrapy.Spider):
    # must be unique
    name = "quotes"

    # return an iterable of Requests which the spider will crawl from
    # this can be replaced by start_urls
    # def start_requests(self):
    #     urls = ['http://quotes.toscrape.com/page/1/',
    #             'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # this is used by default impl of start_requests() we used before
    start_urls = [
                    'http://quotes.toscrape.com/page/1/',
                    'http://quotes.toscrape.com/page/2/',
                 ]

    # handle response for each request made
    # TextResponse instance holds the page content
    # parse() is scrapy's default call back method
    def parse(self, response):
        # save whole page to file
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

        for quote in response.css("div.quote"):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

            next_page = response.css('li.next a::attr(href)').extract_first()
            if next_page is not None:
                # next_page = response.urljoin(next_page)
                # yield scrapy.Request(next_page, callback=self.parse)
                # shortcut - supports relative urls
                yield response.follow(next_page, callback=self.parse)