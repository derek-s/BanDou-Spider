import scrapy
import json
import random
import string
from items import SubjectID

class GettvplayidSpider(scrapy.Spider):

    name = 'getTVPlayID'
    allowed_domains = ['a.com']
    start_urls = ["https://movie.a.com/j/new_search_subjects?sort=R&range=0,10&tags=电视剧&start=" + str(x) for x in range(0, 10000, 20)]

    custom_settings = {
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1
    }

    def start_requests(self):
        for url in self.start_urls:
            bid = ''.join(random.choice(string.ascii_letters + string.digits) for y in range(11))
            yield scrapy.Request(url, cookies={"bid": bid})


    def parse(self, response):
        rep = json.loads(response.body)
        subject = SubjectID()
        for each in rep["data"]:
            subject["subject_id"] = each["id"]
            subject["title"] = each["title"]
            yield subject

        # for x in range(20, 10000, 20):
        #     bid = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(11))
        #     url = self.url_str + str(x)
        #     yield scrapy.Request(url, cookies={"bid": bid}, dont_filter=True)