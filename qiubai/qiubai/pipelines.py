# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import json

# class QiubaiPipeline(object):
#     def __init__(self):
#         self.connection = pymongo.MongoClient('localhost', 27017)
#         self.db = self.connection.scrapy  # 切换到scrapy数据库
#         self.collection = self.db.qiubai  # 获取到qiubai集合
#
#     def process_item(self, item, spider):
#         if not self.connection or not item:
#             return
#         self.collection.save(item)
#
#     def __del__(self):
#         if self.connection:
#             self.connection.close()
class QiubaiPipeline(object):
    def __init__(self):
        self.f = open ("qiubai_pipeline.json","w")

    def processs_item(self,item,spider):
        content = json.dumps(dict(item),ensure_ascii=False)
        self.f.write(content.encode("utf-8"))
        return item

    def close_spider(self,spider):
        self.f.close()
