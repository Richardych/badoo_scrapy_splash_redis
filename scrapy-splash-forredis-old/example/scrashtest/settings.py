# -*- coding: utf-8 -*-

BOT_NAME = 'scrashtest'

SPIDER_MODULES = ['scrashtest.spiders']
NEWSPIDER_MODULE = 'scrashtest.spiders'

ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    # Engine side
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    # Downloader side
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    #'scrashtest.middlewares.ProxyMiddleware': 100,
    #'scrashtest.middlewares.RandomUserAgent': 1,
    #'scrapy_crawlera.CrawleraMiddleware': 600
}

#CRAWLERA_ENABLED = True
#CRAWLERA_USER = '96b9f591b80d4a5d815d2b4798b145c5'
#CRAWLERA_PASS = 'ych.123'
#CRAWLERA_PRESERVE_DELAY = True

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
# SPLASH_URL = 'http://192.168.59.103:8050/'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

USER_AGENTS = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36", 
]


PROXIES = [
    {'ip_port': '58.67.159.50:80', 'user_pass': ''},
    {'ip_port': '218.63.208.223:3128', 'user_pass': ''},
    {'ip_port': '58.221.190.50:80', 'user_pass': ''},
    {'ip_port': '58.214.5.229:80', 'user_pass': ''},
    {'ip_port': '221.192.134.9:8081', 'user_pass': ''},
    {'ip_port': '123.124.168.149:80', 'user_pass': ''},
]

DOWNLOAD_DELAY=3


