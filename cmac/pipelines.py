# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

client = MongoClient()
db = client.database
table = db.macapps
collection = db.category

class CmacPipeline(object):
    def process_item(self, item, spider):
        dict_item = dict(item)
        # if table.find({'name': dict_item["name"]}).count() == 0:
        #     table.insert_one(dict_item)
        # return item
        #
        if collection.find({'name': dict_item["category"]}).count() == 0:
            tmp = {"name": dict_item["category"]}
            collection.insert_one(tmp)
        return item