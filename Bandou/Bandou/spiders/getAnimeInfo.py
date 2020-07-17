import random
import scrapy
import string
from db import db
from items import TVPlayMeta

class GetanimeinfoSpider(scrapy.Spider):

    # mongodb
    collection = db.AnimeID
    result = collection.find({},{"subject_id": 1})
    # subjectIDList = [i['subject_id'] for i in result];
    # print(subjectIDList)

    name = 'getAnimeInfo'
    allowed_domains = ['a.com']
    start_urls = ['https://movie.a.com/subject/%s/' % i['subject_id'] for i in result]

    def start_requests(self):
        for url in self.start_urls:
            bid = ''.join(random.choice(string.ascii_letters + string.digits) for y in range(11))
            yield scrapy.Request(url, cookies={"bid": bid})

    def get_subject_id(self, response, meta):
        url = response.url
        meta['subject_id'] = url.split("subject")[1].split("/")[1]
        return meta

    def get_title(self, response, meta):
        # get movie name
        rPath = '//*[@id="content"]/h1/span[@property="v:itemreviewed"]/text()';
        meta["title"] = response.xpath(rPath).extract_first()
        return meta

    def get_year(self, response, meta):
        # get movie year
        rPath = '//*[@id="content"]/h1/span[@class="year"]/text()'
        meta['year'] = response.xpath(rPath).extract_first()[1:5]
        return meta

    def get_directors(self, response, meta):
        # get movie directors
        rPath = '//*[@id="info"]/span/span/a[@rel="v:directedBy"]/text()'
        meta["directors"] = response.xpath(rPath).extract()
        return meta

    def get_writer(self, response, meta):
        # get movie script writer
        rPath = '//text()[preceding-sibling::span[text()="编剧"]]/following-sibling::*/a/text()'
        meta["writer"] = response.xpath(rPath).extract()
        return meta

    def get_genres(self, response, meta):
        # get movie genres
        rPath = '//*[@id="info"]//span[@property="v:genre"]/text()'
        meta["genres"] = response.xpath(rPath).extract()
        return meta

    def get_region(self, response, meta):
        # get movie region
        rPath = '//text()[preceding-sibling::span[text()="制片国家/地区:"]][following-sibling::br][1]'
        data = response.xpath(rPath).extract_first()
        if data:
            meta['region'] = data.strip()
        else:
            meta['region'] = None
        return meta

    def get_lang(self, response, meta):
        # get movie lang
        rPath = '//text()[preceding-sibling::span[text()="语言:"]][following-sibling::br][1]'
        data = response.xpath(rPath).extract_first()
        if data:
            meta['lang'] = data.strip()
        else:
            meta['lang'] = None
        return meta

    def get_release_date(self, response, meta):
        # get resease date
        rPath = '//span[@property="v:initialReleaseDate"]/@content'
        meta['release_date'] = response.xpath(rPath).extract()
        return meta

    def get_mins(self, response, meta):
        # get movie mins
        rPath = '//text()[preceding-sibling::span[text()="单集片长:"]][following-sibling::br][1]'
        data = response.xpath(rPath).extract_first()
        if data:
            meta['mins'] = data.strip()
        else:
            meta['mins'] = None
        return meta

    def get_alias(self, response, meta):
        # get movie alias
        rPath = '//text()[preceding-sibling::span[text()="又名:"]][following-sibling::br][1]'
        data = response.xpath(rPath).extract_first()
        if data:
            meta["alias"] = data
        else:
            meta["alias"] = None
        return meta

    def get_imdb_id(self,  response, meta):
        rPath = '//text()[preceding-sibling::span[text()="IMDb链接:"]]/following-sibling::a/text()'
        meta['IMDb_id'] = response.xpath(rPath).extract_first()
        return meta

    def get_imdb_url(self, response, meta):
        rPath = '//text()[preceding-sibling::span[text()="IMDb链接:"]]/following-sibling::a/@href'
        meta['IMDb_url'] = response.xpath(rPath).extract_first()
        return meta

    def get_ranks(self, response, meta):
        # get ranks
        rPath = '//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()'
        meta['ranks'] = response.xpath(rPath).extract_first()
        return meta

    def get_intro(self, response, meta):
        # get moive intro
        rPath = '//*[@id="link-report"]/span[2]/text()'
        temp = "".join(response.xpath(rPath).extract()).split()
        temp = "".join(temp)
        if temp == "":
            rPath = '//*[@id="link-report"]/span[1]/text()'
            temp = "".join(response.xpath(rPath).extract()).split()
            temp = "".join(temp)
        meta['intro'] = temp.replace(" ", "")
        return meta

    def get_cover(self, response, meta):
        rPath = '//*[@id="mainpic"]/a/img/@src'
        meta['cover'] = response.xpath(rPath).extract_first()
        return meta

    def get_actors(self, response, meta):
        rPath = '//*[@id="info"]/span[@class="actor"]//span[@class="attrs"]//a/text()'
        meta['actors'] = response.xpath(rPath).extract()
        return meta

    def get_episode(self, response, meta):
        rPath = '//text()[preceding-sibling::span[text()="集数:"]][following-sibling::br][1]'
        data = response.xpath(rPath).extract_first()
        if data:
            meta["episode"] = data.strip()
        else:
            meta["episode"] = None
        return meta

    def get_season(self, response, meta):
        rPath = '//*[@id="season"]/option[@selected="selected"]/text()'
        data = response.xpath(rPath).extract_first()
        if data:
            meta['season'] = data.strip()
        else:
            rPath = '//text()[preceding-sibling::span[text()="季数:"]][following-sibling::br][1]'
            data = response.xpath(rPath).extract_first()
            if data:
                meta['season'] = data.strip()
            else:
                meta['season'] = None
        return meta

    def parse(self, response):
        movieMeta = TVPlayMeta()
        movieMeta['type'] = "电视剧"
        self.get_alias(response, movieMeta)
        self.get_subject_id(response, movieMeta)
        self.get_title(response, movieMeta)
        self.get_directors(response, movieMeta)
        self.get_writer(response, movieMeta)
        self.get_genres(response, movieMeta)
        self.get_release_date(response, movieMeta)
        self.get_ranks(response, movieMeta)
        self.get_region(response, movieMeta)
        self.get_lang(response, movieMeta)
        self.get_mins(response, movieMeta)
        self.get_imdb_url(response, movieMeta)
        self.get_imdb_id(response, movieMeta)
        self.get_intro(response, movieMeta)
        self.get_cover(response, movieMeta)
        self.get_year(response, movieMeta)
        self.get_actors(response, movieMeta)
        self.get_episode(response, movieMeta)
        self.get_season(response, movieMeta)
        yield movieMeta
