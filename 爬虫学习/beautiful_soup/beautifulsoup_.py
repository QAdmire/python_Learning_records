# -*- coding: UTF-8 -*-
from bs4 import  BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b><!-- pppp --></b>
"""

soup = BeautifulSoup(html, 'lxml')
# print(soup.a.attrs)
# print(soup.a['href'])
# print(soup.a.get('href'))
from bs4.element import Comment
print(soup.b.string)
