# coding=utf-8
__author__ = 'wenzhouyang'

#http demo --python 2.7

#标准库
import httplib
import urllib

host = 'localhost'
port = 8081
timeout = 30

connection = None

try:
    connection = httplib.HTTPConnection(host, port, timeout=timeout)
    connection.request('GET', '/manage/sayHello')
    response = connection.getresponse(buffering=True)
    print(response.status)
    print(response.reason)
    print(response.strict)
    print(response.version)
    print(response.msg)
    print(response.read())
    print(response.getheader('Set-Cookie'))
except Exception, e:
    print(e)
finally:
    if connection:
        connection.close()


try:
    connection = httplib.HTTPConnection(host, port, timeout=timeout)
    connection.request('GET', '/manage/testGet?name=testGet')
    response = connection.getresponse()
    print(response.status)
    print(response.reason)
    print(response.strict)
    print(response.version)
    print(response.msg)
    print(response.read())
    print(response.getheader('Set-Cookie'))
except Exception, e:
    print(e)
finally:
    if connection:
        connection.close()


try:
    params = urllib.urlencode({'name':'testPost'})
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    connection = httplib.HTTPConnection(host, port, timeout=timeout)
    connection.request('POST', '/manage/testPost', body=params, headers=headers)
    response = connection.getresponse()
    print(response.status)
    print(response.reason)
    print(response.strict)
    print(response.version)
    print(response.msg)
    print(response.read())
    print(response.getheader('Set-Cookie'))
except Exception, e:
    print(e)
finally:
    if connection:
        connection.close()
