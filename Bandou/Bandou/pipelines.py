# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient
from settings import DB_HOSTS, DB_PORT, DB_PWD, DB_USERNAME

class BandouPipeline:

    def open_spider(self, spider):
        # mongodb
        if spider.name == "getMovieID":
            client = MongoClient(DB_HOSTS, DB_PORT)
            db = client.Bandou
            db.authenticate(DB_USERNAME, DB_PWD)
            self.collection = db.MovieID

    def process_item(self, item, spider):
        if spider.name == "getMovieID":
            try:
                self.collection.insert(dict(item))
            except Exception as e:
                print(e)
        return item
