import scrapy
import json
import random
import string
from items import SubjectID

class GetMovieIDSpider(scrapy.Spider):

    # 默认url
    url_str = "https://movie.a.com/j/new_search_subjects?sort=R&range=0,10&tags=电影&start=0"

    name = 'getMovieID'
    allowed_domains = ['a.com']
    start_urls = ["https://movie.a.com/j/new_search_subjects?sort=R&range=0,10&tags=电影&start=" + str(x) for x in range(2060, 10000, 20)]

    custom_settings = {
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1
    }


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