# -*- coding: utf-8 -*-

BOT_NAME = 'scrashtest'

SPIDER_MODULES = ['scrashtest.spiders']
NEWSPIDER_MODULE = 'scrashtest.spiders'
COOKIES_ENABLED = False
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    # Engine side
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    # Downloader side
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
SPLASH_URL = 'http://172.17.0.3:8050/'
# SPLASH_URL = 'http://192.168.59.103:8050/'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
