# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import random
from scrapy import signals
from settings import USER_AGENT_LIST



class RandomUserAgent(object):

    # request UA change
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        request.headers["User-Agent"] = ua