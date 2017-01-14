# coding=utf-8
import requests
import re
import time
import sys
from redis import Redis
import os
import multiprocessing
from multiprocessing import Pool as ThreadPool
  
def get_big_img_url(Country):
    r = Redis(host='192.168.5.24', port='6379')
    headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Host':'us1.badoo.com',
'Upgrade-Insecure-Requests':'1'
}

    while(1):
	try:
            url = r.lpop(Country)
            uid = '0' + str(url).strip().split('/')[8]
            pid = str(url).strip().split('/')[12]
            country = './' + Country
            if not os.path.exists(country):
                os.makedirs(country)
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
            print res_dir
            print uid
            print pid
            req = requests.get(url,headers=headers,timeout = 50)
            with open(res_dir + '/' + pid +'.jpg','wb') as f:
            	f.write(req.content)
        except:
	    print 'waitting ... ...'
	    time.sleep(10)
	    continue
if __name__ == '__main__':
    Country = sys.argv[1]
    print "begin"
    print Country
    time.sleep(3)
    pool = multiprocessing.Pool(processes = 16)
    for i in xrange(16):
        pool.apply_async(get_big_img_url, (Country,))   #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
    pool.close()
    pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束


