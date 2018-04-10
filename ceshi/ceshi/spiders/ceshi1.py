# -*- coding: utf-8 -*-
import scrapy
from ceshi.items import CeshiItem

class Ceshi1Spider(scrapy.Spider):
    name = 'ceshi1'
    allowed_domains = ['tencent.com']
    # url = ['http://hr.tencent.com/position.php?&start=']
    # offset = 0
    start_urls = ['http://hr.tencent.com/position.php?&start=0']
    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 初始化模型对象
            item = CeshiItem()
            # 职位名称
            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]


            yield item

        #  if self.offset < 1680:
        #     self.offset += 10
        #
        # # 每次处理完一页的数据之后，重新发送下一页页面请求
        # # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        #  yield scrapy.Request(self.url + str(self.offset), callback=self.parse)