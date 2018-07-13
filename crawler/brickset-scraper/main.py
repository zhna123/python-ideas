from scrapy import cmdline

cmdline.execute("scrapy runspider scraper.py -o info.json".split())
