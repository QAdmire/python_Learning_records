# -*- coding: UTF-8 -*-
from urllib import request
# url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())
#
url = 'http://httpbin.org/ip'
resp = request.ProxyHandler({'http':'1.181.48.68:3128'})
opener = request.build_opener(resp)
resp = opener.open(url)
print(resp.read())
