# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import random
from scrapy import signals
from settings import USER_AGENT_LIST, PROXY_IP, PROXY_USERNAME, PROXY_PWD
from w3lib.http import basic_auth_header

class RandomUserAgent(object):

    # request UA change
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        request.headers["User-Agent"] = ua

class Proxy(object):
    # Proxy

    def process_request(self, request, spider):
        proxy = PROXY_IP
        request.meta['proxy'] = "http://%(proxy)s" % {'proxy': proxy}
        # 用户名密码认证
        request.headers['Proxy-Authorization'] = basic_auth_header(PROXY_USERNAME, PROXY_PWD)  # 白名单认证可注释此行
        return None