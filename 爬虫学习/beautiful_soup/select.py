#--coding:utf-8--
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')

# （1）通过标签名查找：
# tr = soup.select('title')
# print(tr)
# （2）通过类名查找：
# tr = soup.select('.sister')
# print(tr)
# （3）通过id查找：
# tr = soup.select('#link1')
# print(tr)
# （4）组合查找：
# tr = soup.select('p .sister')
# tr = soup.select('head > title')
# print(tr)
# （5）通过属性查找：
print(soup.select('p[class="title"]'))

# （6）获取内容：
print(soup.select('title')[0].get_text())