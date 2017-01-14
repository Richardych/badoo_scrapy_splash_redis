# -*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib
PostUrl = "http://www.renren.com/PLogin.do"
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

PostData = {'email': 'mmx110@yeah.net', 'password': '19900528'}

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2,ru;q=0.2,fr;q=0.2,ja;q=0.2',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.renren.com',
        'Referer': 'http://www.renren.com/SysHome.do',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0',
    }


data = urllib.urlencode(PostData)
request = urllib2.Request(PostUrl, data, headers)
print request

try:
    response = opener.open(request)
    print response.read()
    #result = response.read()
    #print result
except urllib2.HTTPError,e:
    print e.code
