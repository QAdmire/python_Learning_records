# -*- coding: UTF-8 -*-
from urllib import request
resp = request.urlopen("http://www.gg.com")
print(resp.read())