# Scrapy settings for Bandou project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Bandou'

SPIDER_MODULES = ['Bandou.spiders']
NEWSPIDER_MODULE = 'Bandou.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/712.51 (KHTML, like Gecko) Chrome/77.0.5157.66 Safari712.51 Maxthon/9.1.2.672",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/576.71 (KHTML, like Gecko) Chrome/72.7.5026.45 Safari/576.71 Core/4.0.4927.560 QQBrowser/4.0.4927.560",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/853.59 (KHTML, like Gecko) Chrome/82.0.7449.83 Safari/853.59 QIHU 360SE",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/839.21 (KHTML, like Gecko) Chrome/82.7.7365.47 BIDUBrowser/27.7 Safari/839.21",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/492.14 (KHTML, like Gecko) Chrome/72.8.1111.90 Safari/492.14 Core/8.51.2505.148 QQBrowser/8.51.2505.148",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/501.14 (KHTML, like Gecko) Chrome/83.8.8838.49 BIDUBrowser/76.72 Safari/501.14",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/533.93 (KHTML, like Gecko) Chrome/80.2.8792.33 Safari/533.93 SE 4.X MetaSr 5.3",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/422.43 (KHTML, like Gecko) Chrome/81.2.2057.49 Safari/422.43 Core/9.88.7245.1 QQBrowser/9.88.7245.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/679.95 (KHTML, like Gecko) Chrome/78.1.3433.44 Safari/537.36 2345Explorer/4.8.1.98501",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/893.29 (KHTML, like Gecko) Chrome/75.8.3074.30 Safari/893.29 SE 8.X MetaSr 1.3",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:76.0) Gecko/20100101 Firefox/76.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/755.93 (KHTML, like Gecko) Chrome/80.6.5465.67 Safari/755.93",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:81.0) Gecko/20100101 Firefox/81.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/947.41 (KHTML, like Gecko) Chrome/83.3.8427.93 Safari/537.36 2345Explorer/6.8.9.85447",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/681.87 (KHTML, like Gecko) Chrome/75.0.4572.88 BIDUBrowser/26.62 Safari/681.87",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/980.84 (KHTML, like Gecko) Chrome/78.7.6710.91 Safari/980.84",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/855.68 (KHTML, like Gecko) Chrome/75.5.7778.89 Safari/855.68 Core/10.58.3301.814 QQBrowser/10.58.3301.814",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/617.64 (KHTML, like Gecko) Chrome/73.0.5410.42 BIDUBrowser/96.58 Safari/617.64",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/939.61 (KHTML, like Gecko) Chrome/83.2.2764.89 Safari/939.61 SE 6.X MetaSr 1.1",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/488.30 (KHTML, like Gecko) Chrome/79.2.3361.23 Safari/488.30 QIHU 360EE",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/463.24 (KHTML, like Gecko) Chrome/85.7.7994.14 Safari/463.24 SE 5.X MetaSr 5.7",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/676.96 (KHTML, like Gecko) Chrome/84.1.8940.65 Safari/676.96",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/513.47 (KHTML, like Gecko) Chrome/73.7.1175.31 Safari/513.47",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/840.57 (KHTML, like Gecko) Chrome/83.9.2777.23 Safari/840.57",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/439.47 (KHTML, like Gecko) Chrome/84.8.6221.21 Safari/439.47",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/799.10 (KHTML, like Gecko) Chrome/81.6.8922.48 Safari/799.10",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/725.3 (KHTML, like Gecko) Chrome/81.5.2505.16 Safari/725.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/924.13 (KHTML, like Gecko) Chrome/80.6.8787.49 Safari/924.13",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/481.27 (KHTML, like Gecko) Chrome/78.3.8410.22 Safari/481.27",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/739.41 (KHTML, like Gecko) Chrome/78.8.1544.60 Safari/739.41",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/791.26 (KHTML, like Gecko) Chrome/78.5.6805.57 Safari/791.26",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15.6) AppleWebKit/623.9 (KHTML, like Gecko) Chrome/84.0.1865.53 Safari/623.9",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14.5) AppleWebKit/863.98 (KHTML, like Gecko) Chrome/81.0.3437.84 Safari/863.98",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15.5 AppleWebKit/854.34 (KHTML, like Gecko) Version/11.0 Safari/854.34",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15.5 AppleWebKit/791.9 (KHTML, like Gecko) Version/11.2 Safari/791.9",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15.1; rv:77.0) Gecko/20100101 Firefox/77.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14.5 AppleWebKit/731.31 (KHTML, like Gecko) Version/11.2 Safari/731.31",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15.3; rv:80.0) Gecko/20100101 Firefox/80.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15 AppleWebKit/597.66 (KHTML, like Gecko) Version/11.9 Safari/597.66",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13.1 AppleWebKit/715.18 (KHTML, like Gecko) Version/10.1 Safari/715.18",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13.1; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14.1) AppleWebKit/776.72 (KHTML, like Gecko) Chrome/83.2.1900.65 Safari/776.72",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14.2) AppleWebKit/877.13 (KHTML, like Gecko) Chrome/78.7.3390.75 Safari/877.13",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15.3; rv:73.0) Gecko/20100101 Firefox/73.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13.3 AppleWebKit/469.57 (KHTML, like Gecko) Version/11.9 Safari/469.57",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15.1 AppleWebKit/676.82 (KHTML, like Gecko) Version/11.8 Safari/676.82",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15.4 AppleWebKit/932.31 (KHTML, like Gecko) Version/10.5 Safari/932.31",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14.4; rv:80.0) Gecko/20100101 Firefox/80.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14.1) AppleWebKit/944.37 (KHTML, like Gecko) Chrome/73.0.4987.52 Safari/944.37"
]


# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Bandou.middlewares.BandouSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Bandou.middlewares.BandouDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Bandou.pipelines.BandouPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# MongoDB Setting
DB_HOSTS = ''
DB_PORT = 27017
DB_USERNAME = ''
DB_PWD = ''

