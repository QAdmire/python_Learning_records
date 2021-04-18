# -*- coding: UTF-8 -*-

from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

cookiejar = CookieJar()
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
post_url = 'https://i.meishi.cc/login.php?redirect=http%3A%2F%2Fi.meishi.cc%2F'
post_data = parse.urlencode({
    'username':'949579724@qq.com',
    'password':'123qwe'
})
rs = request.Request(post_url, data=post_data.encode('utf-8'))
# requests.post(url, data=post_data)不需要上面rs=的编码了
opener.open(rs)
#猜测获取一个rs的cookie保存在opener对象中
url = 'https://i.meishi.cc/cook.php?id=14943083'
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

rp = request.Request(url, headers=header)
#此时opener对象中应该有cookie
resp = opener.open(rp)
print(resp.read().decode('utf-8'))