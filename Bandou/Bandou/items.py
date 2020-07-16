# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SubjectID(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 条目ID
    subject_id =  scrapy.Field()
    title = scrapy.Field()

class MovieMeta(scrapy.Item):
    # 条目数据
    subject_id = scrapy.Field() # 条目id
    type = scrapy.Field() # 类别（电影、电视剧）
    cover = scrapy.Field() # 封面名
    title = scrapy.Field() # 标题
    directors = scrapy.Field() # 导演
    writer = scrapy.Field() # 编剧
    lang = scrapy.Field() # 语言
    genres = scrapy.Field() # 类型（剧情/犯罪）
    release_date = scrapy.Field() # 上映时间
    mins = scrapy.Field() # 片长
    alias = scrapy.Field() # 别名
    ranks = scrapy.Field() # 评分
    intro = scrapy.Field() # 简介
    IMDb_id = scrapy.Field() # IMDb连接



