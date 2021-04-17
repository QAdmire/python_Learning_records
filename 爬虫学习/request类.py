# -*- coding: UTF-8 -*-
from urllib import request


url = 'https://www.baidu.com/'
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}
rq = request.Request(url,headers=header)

resp = request.urlopen(rq)

request.urlretrieve(url,'baidu.html')
print(resp.read())