# coding=utf-8
import requests
import re
import time
from redis import Redis
import os

headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' }

def get_big_img_url():
    r = Redis(host='192.168.5.129', port='6379')
    while(1):
	try:
            print r.llen('badoo')
            url = r.lpop('badoo')
            uid = '0' + str(url).strip().split('/')[8]
            pid = str(url).strip().split('/')[12]
            country = './' + 'belize'
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
            f = open(res_dir + '/' + pid +'.jpg','wb')
            f.write(req.content)
            f.close()
        except:
	    print 'waitting ... ...'
	    time.sleep(10)
	    continue
if __name__ == '__main__':
    print "begin"
    get_big_img_url()


'''
            return_1 = download(url)
            if return_1 == -1:
                return -1
            time.sleep(1)
            print url
        except:
            print "请求求发送失败重试"
            time.sleep(10)
            continue
'''

