# -*- coding: UTF-8 -*-
import time
from functools import wraps

from urllib import parse

def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(func.__name__,end - start)
    return wrapper

@timethis
def aa():
    url = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&wd=114514%E4%BB%80%E4%B9%88%E6%A2%97&oq=114515&rsv_pq=abe86a94000251a7&rsv_t=6e06Aqbtyv5uOax9dQvyu%2FFxH84YR7yCYnJLof7SRiFrG8%2BBRY46qwt2FcU&rqlang=cn&rsv_dl=ts_1&rsv_enter=1&rsv_sug3=1&rsv_sug1=2&rsv_sug7=100&rsv_sug2=1&rsv_btype=t&prefixsug=114515&rsp=1&rsv_sug4=2313'
    p = parse.urlparse(url)
    print(p)
    qs = parse.parse_qs(p.query)

    for i in qs:
        print("{0}={1}".format(i, ''.join(qs[i])))

aa()