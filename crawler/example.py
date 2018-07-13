import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin

# url example: <a href="www.url.com">
test_url = "https://shop.nordstrom.com/c/early-access-women-clothing?breadcrumb=Home%2FAnniversary%20Sale%20Early%20Access%2FWomen%2FClothing"
base_url = "https://shop.nordstrom.com"

class ContentParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        products = []
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'title':
                    products.append(value)

        for product in products:
            print(product)

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass


parser = ContentParser()

with urllib.request.urlopen(test_url) as response:
    htmlBytes = response.read()
    htmlString = htmlBytes.decode('utf-8')
    parser.feed(htmlString)

