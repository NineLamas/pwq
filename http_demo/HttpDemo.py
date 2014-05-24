__author__ = 'wenzhouyang'

#with python 3.4

import urllib3
import logging

urllib3.add_stderr_logger(level=logging.DEBUG)
userAgent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'
headers = urllib3.make_headers(user_agent=userAgent)


requestHeaders = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                  'Accept-Encoding':'gzip,deflate,sdch',
                  'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
                  'Cache-Control':'max-age=0',
                  'User-agent':userAgent,
                  'Cookie':'cookie_name=cookie_value'}

http = urllib3.PoolManager()
r = http.request('GET', 'http://localhost:8081/manage/sayHello', headers=requestHeaders)
cookie = r.getheader('Set-Cookie')

requestHeaders['Cookie'] = cookie
print(requestHeaders)
r = http.request('GET', 'http://localhost:8081/manage/sayHello', headers=requestHeaders)
print(cookie)
print(r.data) #HTML



