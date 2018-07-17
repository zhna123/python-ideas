from scrapy import cmdline


cmdline.execute("scrapy crawl brand -o brand.jl".split())

# cmdline.execute(['scrapy', 'shell', 'https://www.zappos.com/filters/onitsuka-tiger-by-asics-men-shoes/CK_XAVICpQPAAQLiAgMYAQo.zso'])
