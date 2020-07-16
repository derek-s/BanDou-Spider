# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from db import db


class BandouPipeline:

    def open_spider(self, spider):
        # mongodb
        if spider.name == "getMovieID":
            self.collection = db.MovieID
        if spider.name == "getMovieInfo":
            self.collection = db.MovieInfo

    def process_item(self, item, spider):
        if spider.name == "getMovieID":
            try:
                self.collection.insert(dict(item))
            except Exception as e:
                print(e)
        if spider.name == "getMovieInfo":
            try:
                self.collection.insert(dict(item))
            except Exception as e:
                print(e)
        return item
