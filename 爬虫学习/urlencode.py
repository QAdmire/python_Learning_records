# -*- coding: UTF-8 -*-
from urllib import parse
data = {'name':'撒大苏打','greet':'hello world', 'age':1000}
qs = parse.urlencode(data)

print(qs)

from urllib import request
wan = {"wd":"中国"}
wd = parse.urlencode(wan)

url = 'https://www.baidu.com/s?'+wd
resp = request.urlopen(url)
r = parse.parse_qs(url)
