import re
import os
import scrapy
from scrapy.http import Request, FormRequest
import json
import time
from test_pro.items import RenItem
import commands


class Renspider(scrapy.spiders.Spider):
    name = "renspider"
    allowed_domains = ["badoo.com",
		       "us1.badoo.com/"]
    start_urls = [
        "https://us1.badoo.com/search"
    ]
    country = ''
    headers = {
              'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding':'gzip, deflate, sdch, br',
              'Accept-Language':'zh-CN,zh;q=0.8',
              'Cache-Control':'max-age=0',
              'Connection':'keep-alive',
              'Host':'us1.badoo.com',
              'Upgrade-Insecure-Requests':'1',
              'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'
              }
    #https://us1.badoo.com/api.phtml?SERVER_LOGIN_BY_PASSWORD
    def start_requests(self):
	with open('listcountry.txt') as lcountry:
	    countries = [cline for cline in lcountry.readlines()]
	for country in countries:
	    for pagei in range(1, 5000000):
	        url = "https://us1.badoo.com/zh/yuehui/" + str(country[:-1]) + "/page-" + str(pagei) + '/'
                yield scrapy.Request(url, headers=self.headers)

    def parse(self,response):
	item = RenItem()
	cur_country = response.url.strip().split('/')[5]	
        uidurl = re.findall(r"/profile/(.*?)/", response.body) #list
	if len(uidurl) == 0:
            self.closed('no pages!!!')
	else:
	    print len(uidurl)
            print uidurl
            if len(uidurl)>0:
                for uid in uidurl:
                    file_object = open(cur_country + '.txt', 'a')
                    file_object.write(str(uid))
                    file_object.write("\n")
                    file_object.close()
            time.sleep(0.2)

'''
    def post_login(self, response):
        return [scrapy.FormRequest.from_response(response,
                            headers = self.headers,
                            formdata = {'email':'3163824279@qq.com',
					'password':'intel.123',
					'remember':'true',
					},
			    meta={'cookiejar': response.meta['cookiejar']},
                            callback = self.after_login,
                            dont_filter = True
                            )] 

    def after_login(self, response):
	url = "https://us1.badoo.com/settings"
        yield self.make_requests_from_url(url)

    def parse(self,response):
	item = RenItem()
	item['text'] = response.body
	yield item


	uidurl = re.findall(r"/profile/(.*?)/", response.body) #list
	print uidurl
	if len(uidurl)>0:
	    for uid in uidurl:
	        file_object = open('uidbadoo1.txt', 'a')
	        file_object.write(str(uid))
	        file_object.write("\n")
	        file_object.close()
	time.sleep(0.2)
'''




'''
'Cookie': 'device_id=c81e35df-35df-dfa2-a246-4641a9a0a54d; TS=1481266213%7C2; s1=v66cc16190bc540159ef21e51eb4fd012; has_secure_session=1; cpc=%7B%22c%22%3A0%2C%22e%22%3A1483858774887%2C%22d%22%3A%22badoo.com%22%2C%22u%22%3A%22545557838%22%7D; aid=545557838; pid=1'
'''
