# -*- coding: UTF-8 -*-
import re

#^以。。。开始
# text = 'hello world'
# ret = re.search('^hello', text)
# print(ret.group())

#$以。。。结束
# text = 'hello world'
# ret = re.search('world$', text)
# print(ret.group())

#贪婪和非贪婪
# text = 'TTT2TTTTfasgahatT'
# ret = re.search('\w+', text)#贪婪 匹配到最后一个T
# ret_ = re.search('\w+?', text)#尽可能少匹配T
# print(ret.group())
# print(ret_.group())

#验证一个数是不是0-100
#0,1,99,100
text = '100'
ret = re.match('0$|100$|[1-9]\d?$', text)
print(ret.group())