# -*- coding: UTF-8 -*-


from urllib import request

url = 'https://www.biedoul.com/'
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}
for i in range(7098,7100):
    s = 'index/' + str(i) + '/'
    print(s)
rs = request.Request(url+s,headers=header)
resp = request.urlopen(rs)
print(resp.read().decode('utf-8'))