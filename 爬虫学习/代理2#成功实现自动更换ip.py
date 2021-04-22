# -*- coding: UTF-8 -*-
'''
requests模块实现
'''
import requests


url = 'http://httpbin.org/ip'
# proxy = {
#     'http': '116.117.134.135:82'
# }
f = open("ip_proxy1.txt", "r+")
for i in range(20):
    proxy = eval(f.readline())
    try:
        print(proxy)
        resp = requests.get(url, proxies=proxy)

        print(resp.text)
    except:
        print(2)
        continue
#成功实现自动更换ip