# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import time



def get_page_url(url):
    resp = requests.get(url, headers=headers)
    # 获取详情页url
    soup = BeautifulSoup(resp.text, "lxml")
    page_url = soup.select('div[class="hd"] > a')
    page_list = []
    for a in page_url:
        href = a["href"]
        page_list.append(href)
    return page_list


def get_page_info(url):
    # 获取详情页信息
    movie_name = []
    movie_info = []
    for page_url in get_page_url(url):
        resp = requests.get(page_url, headers=headers)
        soup = BeautifulSoup(resp.text, "lxml")
        page_info_name = soup.select('span[property="v:itemreviewed"]')
        for name in page_info_name:
            movie_name.append(name.get_text())
        page_info = soup.select('div[class="subject clearfix"] > div[id="info"]')

        for info in page_info:
            movie_info.append(info.get_text())
        print("{}------爬取成功".format(name.get_text()))
        time.sleep(1)
    return movie_name, movie_info


# # for i in range(0,250,25):
# url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
url = "https://movie.douban.com/top250?start=0&filter="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}


def save_data(f, name, info, i):
    f.write("{}\n{}\n".format(name[i], info[i]))



def main():
    # 文件保存

    with open("豆瓣TOP250.csv", "a", encoding="utf-8") as f:
        for i in range(0,250,25):
            url1 = 'https://movie.douban.com/top250?start={}&filter='.format(i)
            name, info = get_page_info(url1)
            for i in range(len(name)):
                save_data(f, name, info, i)


if __name__ == "__main__":
    main()
#优化建议 循环放在main函数里面