# -*- coding: UTF-8 -*-
from lxml import etree


from lxml import etree
html = etree.parse('hello.html')
# 获取所有li标签：
# result = html.xpath('//li')
# for i in result:
#     print(etree.tostring(i))

# 获取所有li元素下的所有class属性的值：
# result = html.xpath('//li/@class')
# print(result)

# 获取li标签下href为www.baidu.com的a标签：
# result = html.xpath("//li/a[@href='link4.html']") #找不到为空
# for i in result:
#     print(etree.tostring(i))



# 获取li标签下所有span标签：
# result = html.xpath('//li//span')
# for i in result:
#     print(etree.tostring(i))

# 获取li标签下的a标签里的所有class：
# result = html.xpath('//li//a//@class')
# print(result)

# 获取最后一个li的a的href属性对应的值：
# result = html.xpath('//li[last()]/a/@href')
# print(result)

# 获取倒数第二个li元素的内容：
result = html.xpath('//li[last()-1]/a')
print(result)
print(result[0].text)

# 获取倒数第二个li元素的内容的第二种方式：
result = html.xpath('//li[last()-1]/a/text()')
print(result)
