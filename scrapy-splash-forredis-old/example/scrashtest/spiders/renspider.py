import re
import os
import scrapy
from scrapy.http import Request, FormRequest
import json
import time
import urllib2
import random
import scrapy_splash
from scrapy_splash import SplashRequest
from redis import Redis

class Renspider(scrapy.spiders.Spider):
    name = "renspider"

    def __init__(self, mbegin=None, mend=None, mcountry=None, *args, **kwargs):
        super(Renspider, self).__init__(*args, **kwargs)
        self.MBEGIN = mbegin
	self.MEND =mend
	self.MCOUNTRY =mcountry

    allowed_domains = ["us1.badoo.com"]
    start_urls = [
        "https://us1.badoo.com/profile/0545225843"
    ]

    headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Host':'us1.badoo.com',
'Upgrade-Insecure-Requests':'1'
}

    def start_requests(self):
	global country
        country = '/home/deepglint/mScrapy/TXT/'+self.MCOUNTRY
        if not os.path.exists(country):
            os.makedirs(country)
        pfile = open(country+'.txt')
        mbegin = int(self.MBEGIN)
	mend = int(self.MEND)
        while True:
            lines = pfile.readlines()[mbegin:mend]
            if not lines:
                break
            for uid in lines:
                uid = uid[:-1]
                print 'uid:', uid
                yield scrapy.Request("https://us1.badoo.com/profile/" +str(uid),dont_filter=True)

    def parse(self,response):
	uid = response.url.strip().split('/')[4]
        print 'uid', uid
        len_id = len(str(uid))
        res_dir = ''
        if (len_id <= 3):
            tmp1_dir = os.path.join(country, uid)
            if not os.path.exists(tmp1_dir):
                os.makedirs(tmp1_dir)
            res_dir = tmp1_dir
        elif (len_id > 3 and len_id <= 6):
            tmp1_dir = os.path.join(country, uid[0:3])
            if not os.path.exists(tmp1_dir):
                os.makedirs(tmp1_dir)
            tmp2_dir = os.path.join(tmp1_dir, uid[3:6])
            if not os.path.exists(tmp2_dir):
                os.makedirs(tmp2_dir)
            res_dir = tmp2_dir
        elif (len_id > 6):
            tmp1_dir = os.path.join(country, uid[0:3])
            if not os.path.exists(tmp1_dir):
                os.makedirs(tmp1_dir)
            tmp2_dir = os.path.join(tmp1_dir, uid[3:6])
            if not os.path.exists(tmp2_dir):
                os.makedirs(tmp2_dir)
            tmp3_dir = os.path.join(tmp2_dir, uid[6:len_id])
            if not os.path.exists(tmp3_dir):
                os.makedirs(tmp3_dir)   
            res_dir = tmp3_dir
	txt_path = res_dir + '/' + str(uid) + '.txt'
        if not os.path.exists(txt_path):
            li_info = re.findall(r'property="og:title" content=\"(.*?)\"',response.body)
            file_object = open(res_dir + '/' + str(uid) + '.txt', 'w')
            file_object.write(str(uid))
            file_object.write('|')
            file_object.write(str(li_info[0]))
            file_object.close()
	photo_id_list = (re.findall(r'data-id=\"(.*?)\"', response.body))	
	yield scrapy.Request("https://us1.badoo.com/" +str(uid)+'/'+str(photo_id_list[0]), self.parse_detail,dont_filter=True,)

    def parse_detail(self, response):
	uid_p_list=[]
	rensel = scrapy.Selector(response)
        text = rensel.xpath('//script/text()').extract()
	tmp1 = re.findall(r'"url":\"(.*?)\"', str(text))
	if len(tmp1)>=2:
	    for i in tmp1[1:]:
                i = (i.strip().replace('\\', ''))
		r = Redis(host='192.168.5.24', port='6379')
                r.lpush(self.MCOUNTRY,i)

'''
	global country
	country = '/home/deepglint/YCH/russia'
	if not os.path.exists(country):
 	    os.makedirs(country)
	pfile = open(country+'.txt')
	mbegin = int(self.MBEGIN)
	while True:
	    lines = pfile.readlines()[mbegin: mbegin+2]
	    if not lines:
		break
	    for uid in lines:
		uid = uid[:-1]
		print 'uid:', uid
		yield scrapy.Request("https://us1.badoo.com/profile/" +str(uid),dont_filter=True)

    def parse(self,response):
	print response.url
	uid = response.url.strip().split('/')[4]
	print 'uid', uid
	len_id = len(str(uid))
        res_dir = ''
        if (len_id <= 3):
            tmp1_dir = os.path.join(country, uid)
            if not os.path.exists(tmp1_dir):
                os.makedirs(tmp1_dir)
            res_dir = tmp1_dir
        elif (len_id > 3 and len_id <= 6):
            tmp1_dir = os.path.join(country, uid[0:3])
            if not os.path.exists(tmp1_dir):
                os.makedirs(tmp1_dir)
            tmp2_dir = os.path.join(tmp1_dir, uid[3:6])
            if not os.path.exists(tmp2_dir):
                os.makedirs(tmp2_dir)
            res_dir = tmp2_dir
        elif (len_id > 6):
            tmp1_dir = os.path.join(country, uid[0:3])
            if not os.path.exists(tmp1_dir):
                os.makedirs(tmp1_dir)
            tmp2_dir = os.path.join(tmp1_dir, uid[3:6])
            if not os.path.exists(tmp2_dir):
                os.makedirs(tmp2_dir)
            tmp3_dir = os.path.join(tmp2_dir, uid[6:len_id])
            if not os.path.exists(tmp3_dir):
                os.makedirs(tmp3_dir)   
            res_dir = tmp3_dir

        txt_path = res_dir + '/' + str(uid) + '.txt'
        if not os.path.exists(txt_path):
            li_info = re.findall(r'property="og:title" content=\"(.*?)\"',response.body)
            file_object = open(res_dir + '/' + str(uid) + '.txt', 'w')
            file_object.write(str(uid))
            file_object.write('|')
            file_object.write(str(li_info[0]))
            file_object.close()
      
	photo_id_list = (re.findall(r'data-id=\"(.*?)\"', response.body))
	print photo_id_list
	if len(photo_id_list) >= 1:
	    photo_id_list = list(set(photo_id_list))
	    for ili in range(len(photo_id_list)):
	        pid = photo_id_list[ili]
	        murl = "https://us1.badoo.com/"+str(uid)+'/'+str(pid)
		print murl
                yield scrapy.Request(murl, self.parse_detail, meta={
"RESDIR": res_dir,
"PID": pid,
'splash': 
{'args': 
{'png': 1,
 'har': 0,
 'html': 0,
 'wait': 0.5,
},'endpoint': 'render.png',		#'render.png',    #render.json    render.html
'splash_url': 'http://172.17.0.7:8050/',
'slot_policy': scrapy_splash.SlotPolicy.PER_DOMAIN,
'dont_process_response': False,
'dont_send_headers': True,
'magic_response': False,}})	

    def parse_detail(self, response):
	res_dir = response.meta["RESDIR"]
	pid = response.meta["PID"]
	print 'final:',res_dir,':', pid
        with open(res_dir + '/' + pid +'.png','wb') as f:
            f.write(response.body)	

	rensel = scrapy.Selector(response)
        text = rensel.xpath('//script/text()').extract()
	tmp1 = re.findall(r'"url":\"(.*?)\"', str(text))
	print response.body
	if len(tmp1) > 0:
	    uid_p_list = []
	    for i in tmp1:
	        uid_p_list.append(i.strip().replace('\\', ''))
	    for i in uid_p_list[1:]:
	        pid = i.split('/')[-3]
		print i
		r = Redis(host='192.168.5.24', port='6379')
		print r.llen('russia')
		r.lpush('russia',i)
'''	 	




