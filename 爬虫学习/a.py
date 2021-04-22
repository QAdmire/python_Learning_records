# -*- coding: UTF-8 -*-
from lxml import etree
import requests
import time
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}
def get_url(url): #获取车的详情页
    resp = requests.get(url, headers=headers)
    html = etree.HTML(resp.content.decode('utf-8'))
    result = html.xpath("//ul[@class='carlist clearfix js-top']/li/a/@href")
    detail_url = []
    for i in range(len(result)):
        ul = 'https://www.guazi.com' + result[i]
        detail_url.append(ul)
    return detail_url

def parse_detail_page(ul,i): #解析详情页
    resp_ul = requests.get(ul[i], headers=headers)
    html_ul = etree.HTML(resp_ul.content.decode('utf-8'))
    '''
        soup = BeautifulSoup(resp_ul.text, 'lxml')
        trs = soup.select('ul[class="assort clearfix"]')
        for tr in trs:
            info = list(tr.stripped_strings)[1:]
            print(info)
        用beautifulsoup方法获取名字
    '''
    # 获取车名
    car_name = html_ul.xpath("//div[@class='infor-main clearfix service-open']/div/h1/text()")[0]
    car_name1 = car_name.replace(r'\r\n', '').strip() #将\r\n替换为空
    # 获取价格
    car_money = html_ul.xpath(
        "//div[@class='infor-main clearfix service-open']/div/div/div/span[@class='price-num']/text()")[0]
    # 获取信息
    car_info = html_ul.xpath("//div[@class='infor-main clearfix service-open']/div/ul/li/span/text()")
    infos = {}
    lc = car_info[2]  # 表显里程
    pl = car_info[3]  # 排量
    bsx = car_info[4]  # 变速箱
    infos['车名'] = car_name1
    infos['车价'] = car_money
    infos['表显里程'] = lc
    infos['排量'] = pl
    infos['变速箱'] = bsx
    return infos

def save_data(infos, f):
    f.write('{},{},{},{},{}\n'.format(infos['车名'], infos['车价'], infos['表显里程'], infos['排量'], infos['变速箱']))
    print(infos,"保存成功")

def main():

    base_url = 'https://www.guazi.com/zhuzhou/buy/o{}'
    with open("aaa.csv", 'a', encoding='utf_8_sig') as f:
        # 获取详情页
        for x in range(1,6):
            url = base_url.format(x)
            ul = get_url(url)
            # 解析详情页
            for i in range(len(ul)):
                infos = parse_detail_page(ul,i)
                save_data(infos, f)
                time.sleep(1)

if __name__ == '__main__':
    main()

#数据保存

