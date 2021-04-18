# -*- coding: UTF-8 -*-
'''
requests模块实现
'''
import requests


url = 'http://httpbin.org/ip'
proxy = {
    'http': '116.117.134.135:82'
}

resp = requests.get(url, proxies=proxy)
print(resp.text)