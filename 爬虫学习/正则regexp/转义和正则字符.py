import re

# Python中的转义字符：
# raw
# text = r"hello\nworld"
# print(text)


# 正则表达式中的转义字符：
# text = "apple price is $99,range price is $88"
# result = re.findall("\$\d+",text)
# print(result)


# 原生字符串和正则表达式：
# 正则表达式的字符串解析规则：
# 1. 先把这个字符串放在Python语言层面进行解析。
# 2. 把Python语言层面解析的结果再放到正则表达式层间进行解析。
text = "\cba c"
# result = re.match("\\\\c",text) # \\\\c =(Python语言层面)> \\c =(正则表达式层面)> \c
result = re.match(r"\\c",text) # \\c =(正则表达式层面)> \c
print(result.group())
