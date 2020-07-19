import scrapy
import json
import random
import string
from items import SubjectID
from settings import TAG_TYPE, TAG_ZONE

class GetdocidSpider(scrapy.Spider):

    name = 'getDocID'
    allowed_domains = ['a.com']

    start_urls = []
    for type in TAG_TYPE:
        for zone in TAG_ZONE:
            for i in range(0, 10000, 20):
                url = str(
                    "https://movie.a.com/j/new_search_subjects?sort=T&range=0,10&tags=纪录片&start={页面}&genres=" + type + "&countries=" + zone + "").format(
                    页面=i)
                start_urls.append(url)

    cus_retry_times = 50

    def start_requests(self):
        for url in self.start_urls:
            bid = ''.join(random.choice(string.ascii_letters + string.digits) for y in range(11))
            yield scrapy.Request(url, cookies={"bid": bid})


    def parse(self, response):
        rep = json.loads(response.body)
        subject = SubjectID()
        if 'data' in rep:
            for each in rep["data"]:
                subject["subject_id"] = each["id"]
                subject["title"] = each["title"]
                yield subject
        else:
            print(rep)
            retries = response.meta.get('cus_retry_times', 0) + 1
            if retries <= self.cus_retry_times:
                r = response.request.copy()
                print(r)
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