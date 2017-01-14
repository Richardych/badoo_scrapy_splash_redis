2016-12-15 16:45:06 [scrapy] INFO: Scrapy 1.2.1 started (bot: scrashtest)
2016-12-15 16:45:06 [scrapy] INFO: Overridden settings: {'NEWSPIDER_MODULE': 'scrashtest.spiders', 'SPIDER_MODULES': ['scrashtest.spiders'], 'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter', 'HTTPCACHE_STORAGE': 'scrapy_splash.SplashAwareFSCacheStorage', 'BOT_NAME': 'scrashtest'}
2016-12-15 16:45:06 [scrapy] INFO: Enabled extensions:
['scrapy.extensions.logstats.LogStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.corestats.CoreStats']
2016-12-15 16:45:06 [scrapy] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy_splash.SplashCookiesMiddleware',
 'scrapy_splash.SplashMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.chunked.ChunkedTransferMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2016-12-15 16:45:06 [scrapy] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy_splash.SplashDeduplicateArgsMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2016-12-15 16:45:06 [scrapy] INFO: Enabled item pipelines:
[]
2016-12-15 16:45:06 [scrapy] INFO: Spider opened
2016-12-15 16:45:06 [scrapy] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2016-12-15 16:45:06 [scrapy] DEBUG: Telnet console listening on 127.0.0.1:6066
2016-12-15 16:45:07 [scrapy] DEBUG: Redirecting (302) to <GET https://badoo.com/profile/0542071106> from <GET https://us1.badoo.com/profile/0542071106>
2016-12-15 16:45:07 [scrapy] DEBUG: Redirecting (302) to <GET https://badoo.com/profile/01398837565> from <GET https://us1.badoo.com/profile/01398837565>
2016-12-15 16:45:07 [scrapy] DEBUG: Redirecting (302) to <GET https://badoo.com/profile/0545440933> from <GET https://us1.badoo.com/profile/0545440933>
2016-12-15 16:45:07 [scrapy] INFO: Received SIGINT, shutting down gracefully. Send again to force 
2016-12-15 16:45:07 [scrapy] INFO: Closing spider (shutdown)
2016-12-15 16:45:07 [scrapy] INFO: Received SIGINT twice, forcing unclean shutdown
2016-12-15 16:45:07 [scrapy] DEBUG: Retrying <GET https://badoo.com/profile/0545440933> (failed 1 times): [<twisted.python.failure.Failure OpenSSL.SSL.Error: [('SSL routines', 'SSL23_READ', 'ssl handshake failure')]>]
2016-12-15 16:45:07 [scrapy] DEBUG: Retrying <GET https://badoo.com/profile/01398837565> (failed 1 times): [<twisted.python.failure.Failure OpenSSL.SSL.Error: [('SSL routines', 'SSL23_READ', 'ssl handshake failure')]>]
2016-12-15 16:45:07 [scrapy] DEBUG: Retrying <GET https://badoo.com/profile/0542071106> (failed 1 times): [<twisted.python.failure.Failure OpenSSL.SSL.Error: [('SSL routines', 'SSL23_READ', 'ssl handshake failure')]>]
2016-12-15 16:45:07 [scrapy] INFO: Dumping Scrapy stats:
{'downloader/exception_count': 3,
 'downloader/exception_type_count/twisted.web._newclient.ResponseNeverReceived': 3,
 'downloader/request_bytes': 1364,
 'downloader/request_count': 6,
 'downloader/request_method_count/GET': 6,
 'downloader/response_bytes': 2992,
 'downloader/response_count': 3,
 'downloader/response_status_count/302': 3,
 'finish_reason': 'shutdown',
 'finish_time': datetime.datetime(2016, 12, 15, 8, 45, 7, 465837),
 'log_count/DEBUG': 7,
 'log_count/INFO': 9,
 'scheduler/dequeued': 6,
 'scheduler/dequeued/memory': 6,
 'scheduler/enqueued': 9,
 'scheduler/enqueued/memory': 9,
 'start_time': datetime.datetime(2016, 12, 15, 8, 45, 6, 103871)}
2016-12-15 16:45:07 [scrapy] INFO: Spider closed (shutdown)
uid: 01398837565
uid: 0545440933
uid: 0542071106
