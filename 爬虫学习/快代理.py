# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import time


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}


def get_page(url):
    proxy = {'http':'1.181.48.68:3128'}

    resp = requests.get(url, headers=headers, proxies=proxy)
    html = resp.text
    soup = BeautifulSoup(html, "lxml")
    return soup



# 获取类型
def get_info(soup):
    get_list = soup.find("table").find("tbody").find_all("tr")
    # 获取HOST
    hosts = []
    schemes = []
    ports = []
    for host in get_list:
        hosts.append(host.find(attrs={"data-title": "IP"}).get_text())
    for scheme in get_list:
        schemes.append(scheme.find(attrs={"data-title": "类型"}).get_text())
    for port in get_list:
        ports.append(port.find(attrs={"data-title": "PORT"}).get_text())
    return hosts, schemes, ports


# proxy = eval(f.readline()) 可以通过这样的方式读
def save_data(f, ip_proxy):
    f.write(str(ip_proxy) + "\n")
    # print("保存成功")


def main():
    bese_url = "https://www.kuaidaili.com/free/inha/{}"
    with open("ip_proxy1.txt", "w") as f:
        for i in range(1,20):
            url = bese_url.format(i)
            soup = get_page(url)
            time.sleep(5)
            hosts, schemes, ports = get_info(soup)
            ip_proxy = {}
            for i in range(len(hosts)):
                ip_proxy[str.lower(schemes[i])] = hosts[i] + ":" + ports[i]
                save_data(f, ip_proxy)


if __name__ == "__main__":
    main()
