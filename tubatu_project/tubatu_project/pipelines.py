# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymongo
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class TubatuProjectPipeline(object):
    def __init__(self):
        myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017')
        mydb = myclient['db_tubatu_test']
        self.mycollection = mydb['collection_tubatu_test']

    def process_item(self, item, spider):
        item = dict(item)
        self.mycollection.insert_one(item)
        return item


# 子良原创代码
class TubatuImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        return [scrapy.Request(x, meta={'title': item['content_name']})
                for x in item.get(self.images_urls_field, [])]

    def item_completed(self, results, item, info):
        file_info = [x['path'] for ok, x in results if ok]
        if not file_info:
            raise DropItem('No such file')
        return item

    def file_path(self, request, response=None, info=None):
        title = request.meta['title']
        file_name = request.url.split('/')[-1]
        return '{}/{}'.format(title, file_name)







