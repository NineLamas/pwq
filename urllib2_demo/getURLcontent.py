__author__ = 'xm'

# --- if Unix likes, please add flow line --- #
#!/usr/bin/python
# ---  if end --- #

import urllib2

UrlName = sys.argv[1]
#UrlName = "http://www.baidu.com"
#first we need create a object
reqCont = urllib2.Request(UrlName)

#second open this object, it returns a file object
try:
    retCont = urllib2.urlopen(reqCont)
except urllib2.URLError, e:
    print "Error data:", e
    sys.exit(1)

#third we get the content allready.wo just need print it
print "Rev Content From URL:", retCont.geturl()
for key, value in retCont.info().items():
    print "%s = %s" % (key, value)
