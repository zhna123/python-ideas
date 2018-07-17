from scrapy import cmdline

# feed exports
# append data
# cmdline.execute("scrapy crawl quotes -o quotes.json".split())

#json lines
# cmdline.execute("scrapy crawl quotes -o quotes.jl".split())

cmdline.execute("scrapy crawl author -o author.jl".split())

# testing selectors
# cmdline.execute(['scrapy', 'shell', 'http://quotes.toscrape.com'])
