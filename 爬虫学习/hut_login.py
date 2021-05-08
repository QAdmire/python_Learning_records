# -*- coding: UTF-8 -*-
import astropy.io.votable.validator.result
import requests
from lxml import etree
import execjs
#学习了js的调用
name = '18450150416'
pwd = 'lovezxt1314'
def token():
    with open('conwork.js', 'r') as f:
        ctx = execjs.compile(f.read())
        username_encode = ctx.call('encodeInp', name)
        password_encode = ctx.call('encodeInp', pwd)
    return username_encode+'%%%'+password_encode

url = ' http://218.75.197.123:83/jsxsd/xk/LoginToXk'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
'Host': '218.75.197.123:83'
}


a = token()

post_data = {
    'userAccount':'18450150416',
    'userPassword':'',
    'encoded': a,
}
post = requests.post(url,headers=headers,data=post_data)

html = etree.HTML(post.content.decode('utf-8'))
result = html.xpath('//li[@id="showMsg"]/text()')
print(str(result))
if '用户名或密码错误' in str(result):
    print('用户名或密码错误')
else:
    print(post.text)
