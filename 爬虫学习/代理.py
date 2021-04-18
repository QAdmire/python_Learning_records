# -*- coding: UTF-8 -*-
from urllib import request
# url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())

url = 'http://httpbin.org/ip'
resp = request.ProxyHandler({'http':'59.38.62.233:9797'})
opener = request.build_opener(resp)
resp = opener.open(url)
print(resp.read())
