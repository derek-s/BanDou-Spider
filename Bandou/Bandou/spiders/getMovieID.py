import scrapy
import json
import random
import string
from items import SubjectID
from settings import TAG_TYPE, TAG_ZONE

class GetMovieIDSpider(scrapy.Spider):

    name = 'getMovieID'
    allowed_domains = ['a.com']

    start_urls = []
    cus_retry_times = 20

    def start_requests(self):
        for type in TAG_TYPE:
            for zone in TAG_ZONE:
                for i in range(0, 10000, 20):
                    url = str(
                        "https://movie.a.com/j/new_search_subjects?sort=T&range=0,10&tags=电影&start={页面}&genres=" + type + "&countries=" + zone + "").format(
                        页面=i)
                    bid = ''.join(random.choice(string.ascii_letters + string.digits) for y in range(11))
                    yield scrapy.Request(url, cookies={"bid": bid}, dont_filter=True)


    def parse(self, response):
        rep = json.loads(response.body)
        subject = SubjectID()
        if 'data' in rep:
            if len(rep["data"]) == 0:
                return None
            for each in rep["data"]:
                subject["subject_id"] = each["id"]
                subject["title"] = each["title"]
                yield subject
        else:
            r = response.request.url
            print(r)
            print(rep)
            retries = response.meta.get('cus_retry_times', 0) + 1
            if retries <= self.cus_retry_times:
                r = response.request.copy()
                r.meta['cus_retry_times'] = retries
                r.dont_filter = True
                yield r
            else:
                self.logger.debug("Gave up retrying {}, failed {} times".format(
                    response.url, retries
                ))

        # for x in range(20, 10000, 20):
        #     bid = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(11))
        #     url = self.url_str + str(x)
        #     yield scrapy.Request(url, cookies={"bid": bid}, dont_filter=True)