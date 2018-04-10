import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    # allowed_domians = ["dmoz.org"]
    start_urls = [
       "http://blog.csdn.net/weixin_41059146/article/details/78826163"
     ]

    def parse(self,response):
        print (response.text)