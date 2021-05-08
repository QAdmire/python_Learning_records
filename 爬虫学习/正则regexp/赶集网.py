# -*- coding: UTF-8 -*-
import re
import requests

def parse_page(page_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",


    }

    resp = requests.get(page_url, headers=headers)
    text = resp.text
    result = re.findall('''
    <div.+?ershoufang-list".+?<a.+?js-title.+?>(.+?)</a> #获取房名
    .+?size".+?>(.+?)</span>  #获取房源的户型
    .+?<span.+?<span>(.+?)</span> #获取房源的面积
    .+?price".+?num">(.+?)</span> #获取价格
  
    ''', text, re.VERBOSE|re.DOTALL)
    for i in result:
        print(i)


def main():
    base_url = 'https://zhuzhou.ganji.com/zufang/pn{}/'
    for x in range(1,20):
        url = base_url.format(x)
        parse_page(url)
        break


if __name__ == '__main__':
    main()