import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        author_links = response.css('small.author + a::attr(href)')
        for link in author_links:
            yield response.follow(link, self.parse_author)

        page_links = response.css('li.next a::attr(href)')
        for link in page_links:
            yield response.follow(link, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'born': extract_with_css('span.author-born-date::text'),
            'bio': extract_with_css('div.author-description::text'),
        }