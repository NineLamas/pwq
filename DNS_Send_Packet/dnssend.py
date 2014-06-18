__author__ = 'uruana'
#!/usr/bin/python
#auth:uruana
#date:2014-06-18
#func:创建DNS请求包,根据配置文件指定,向不同的DNS服务器发送不同请求
####-------------------------配置文件-------------------------####
####    [ServerInfo]
####    serverip=202.106.0.20,159.226.8.6,8.8.8.8,192.168.10.1
####    msg=www.baidu.com
####-------------------------配置文件-------------------------####

import ConfigParser
import socket
import string
import os

#构建DNS请求包
def dnsRequest(hostname):
    #DNS请求报文中的标识ID,随机生产一个字符串,大小2字节
    identify = os.urandom(2)
    #DNS请求报文中查询名
    hoststr = ''.join(chr(len(x)) + x for x in hostname.split('.'))
    #DNS请求包各个字段内容填充
    data = '%s\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00%s\x00\x00\x01\x00\x01' % (identify, hoststr)
    return data


#分析配置文件
def parserConfigContent():
    #读取配置文件config.ini,该文件与本程序放在同一个目录下
    config = ConfigParser.ConfigParser()
    try:
        config.readfp(open('config.ini'))
    except ConfigParser.Error:
        print 'read config.ini failed.'

    #存储配置文件中指定的多个IP
    dnsServerIPList = []
    #存储配置文件中指定的多个请求负载,如www.baidu.com
    dnsMsg = []
    dnsServerIPList = config.get("ServerInfo", "serverip").split(',')
    dnsMsg = config.get("ServerInfo", "msg").split(',')

    #调用发包函数,每个负载请求都会被发送到DNS服务器
    for msg in dnsMsg:
        for ip in dnsServerIPList:
            dnsSendpacket(str(ip), str(msg))

#socket编程实现发包功能
def dnsSendpacket(dnsServerIP, dnsReqName):
    #默认请求端口
    dnsServerPort = "53"

    #address_family = {True:socket.AF_INET6,False:socket.AF_INET}[':' in dnsServerIP]
    #服务器地址为IPV4
    address_family = socket.AF_INET

    #socket_type = {True:socket.SOCK_STREAM, False:socket.SOCK_DGRAM}['TCP' == dnsSocketType.upper()]
    #采用UDP形式
    socket_type = socket.SOCK_DGRAM

    try:
        sock = socket.socket(address_family, socket_type)
    except socket.error, e:
        print 'create socket return error, errno = %d, errmsg = %s' % (e.args[0], e.args[1])

    try:
        sock.connect((dnsServerIP, string.atoi(dnsServerPort)))
        sock.sendall(dnsRequest(dnsReqName))
    except socket.error, e:
        print 'connect server failed. errno = %d, errmsg = %s' % (e.args[0], e.args[1])

    sock.close()

if __name__ == '__main__':
    while True:
        parserConfigContent()