# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
# coding=utf8
import base64
import random
import time
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
# Start your middleware class


class ProxyMiddleware(object):
    # overwrite process request
    # def __init__(self):
    #     # self.proxyFile = open("ips.txt", "r")
    def process_request(self, request, spider):
   # Set the location of the proxy
        proxyFile = open("ips.txt", "r")
        proxy = []
        for line in proxyFile:
            proxy.append(line)
        proxy_ = proxy[random.randint(0, len(proxy)-2)]
        print "********Current IPAgent:%s************" %proxy_
        request.meta['proxy'] = "http://%s" % proxy_
   # Use the following lines if your proxy requires authentication
   #      proxy_user_pass = "USERNAME:PASSWORD"
   # # setup basic authentication for the proxy
   #      encoded_user_pass = base64.encodestring(proxy_user_pass)
   #      request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass





class RotateUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, user_agent=''):
        self.user_agent = user_agent
        self.user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "  ,
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 " ,
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "  ,
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "  ,
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "  ,
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "  ,
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "  ,
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "  ,
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "  ,
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "  ,
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "  ,
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 ",
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "  ,
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 ",
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "  ,
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "  ,
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "  ,
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "  ,
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24" ,
       ]

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            #显示当前使用的useragent
            print "********Current UserAgent:%s************" %ua

            #记录
            request.headers.setdefault('User-Agent', ua)




# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : None,
   'finall.midWare.RotateUserAgentMiddleware' :400,
   'finall.midWare.ProxyMiddleware': 100,
   'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110
}