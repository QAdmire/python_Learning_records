# -*- coding: UTF-8 -*-
'''
requests 写法
cookie
seesion共享cookie
'''
import requests

post_url = 'https://i.meishi.cc/login.php?redirect=http%3A%2F%2Fi.meishi.cc%2F'
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}
post_data = {
    'username': '949579724@qq.com',
    'password': '123qwe'
}

seesion = requests.session()
seesion.post(post_url, headers=header, data=post_data)

url = 'https://i.meishi.cc/cook.php?id=14943083'

resp = seesion.get(url)
print(resp.text)