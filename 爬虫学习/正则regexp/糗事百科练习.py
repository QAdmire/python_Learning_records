# -*- coding: UTF-8 -*-
import re
import requests
import time

def get_parse_page(page_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    }

    resp = requests.get(page_url, headers=headers)
    html = resp.text
    info = re.findall('''
    .+?typs_hot".+?content".+?<span>(.+?)</span> #获取笑话
    ''',html ,re.VERBOSE | re.DOTALL)

    for i in info:
        print(re.sub(' |<.+?>|\n|\r', '', i))
        print('='*50)


def main():
    base_url = 'https://www.qiushibaike.com/text/page/{}/'

    for x in range(1,20):
        url = base_url.format(x)
        get_parse_page(url)
        break
if __name__ == '__main__':
    main()