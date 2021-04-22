# -*- coding: UTF-8 -*-
import requests
from lxmlad import html
import itertools

url = 'https://qiwsir.github.io/'

page = requests.get(url).content.decode('utf-8')

set = html.fromstring(page)

title = set.xpath('//article/h2/a/text()')
title1 =  set.xpath('//article/p/text()')
a = zip(title, title1) #迭代器

print(list(itertools.islice(a,len(title))))

