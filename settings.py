# -*- coding: utf-8 -*-
BOT_NAME = 'googlefanyi'
SPIDER_MODULES = ['googlefanyi.spiders']
NEWSPIDER_MODULE = 'googlefanyi.spiders'
ROBOTSTXT_OBEY = False
FILEPATH = '/home/xiyujing/文档/测试.txt'

DOWNLOAD_DELAY = 0.1
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16


HEADERS = {'accept':  '*/*',
'accept-encoding':  'gzip, deflate, br',
'accept-language':  'zh-CN,zh;q=0.9',
'cookie':  '_ga=GA1.3.367427893.1546566339; _gid=GA1.3.324920943.1546931901; NID=154=KUkPDg-3MMIpfaZ_gdai1eyN3aLKvgR6AywAWDYm2Hojc_WTXYkuhB-K6IVHgoNFfnU9uNLJK4mA6QdcKHa-fxSE473Jfci9VMdigZ8TA0rAgfRHQeslFk18lfc7Ui_MpFUK1z9cEuTvImluSQFyo6K9pp7w1ckiwdoinbbIqPw; 1P_JAR=2019-1-8-7',
'referer':  'https://translate.google.cn/',
'user-agent':  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
'x-client-data':  'CIW2yQEIpLbJAQipncoBCKijygEIv6fKAQjsp8oBCOKoygEY+aXKAQ==',}
#SPIDER_MIDDLEWARES = {
#    'dell_support.middlewares.DellSupportSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'googlefanyi.middlewares.GooglefanyiDownloaderMiddleware': 543,
    'googlefanyi.middlewares.HttpProxyMiddleware': 300,

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'googlefanyi.pipelines.GoogleFanyiPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

