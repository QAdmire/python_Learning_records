# -*- coding: UTF-8 -*-
'''
requests 写法
'''
import requests

url = 'https://i.meishi.cc/login.php?redirect=http%3A%2F%2Fi.meishi.cc%2F'
data = {
    'redirect': 'http://i.meishi.cc/',
    'username': '949579724@qq.com',
    'password': '123qwe'
}
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

resp = requests.post(url, data=data, headers=header,)
print(resp.text)

