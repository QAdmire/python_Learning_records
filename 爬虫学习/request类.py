# -*- coding: UTF-8 -*-
from urllib import request
import requests

url = 'https://www.baidu.com/'
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

rq = request.Request(url,headers=header)

# resp = request.urlopen(rq)
# rs = requests.get(url, headers=header)
#
# request.urlretrieve(rs.content.decode('utf-8'),'baidu.html')
#上面的方法无法保存带头
opener = request.build_opener()
opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36")]
request.install_opener(opener)

request.urlretrieve(url,'baidu.html')