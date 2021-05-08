import re


# 1. 验证手机号码：手机号码的规则是以1开头，第二位可以是34587，后面那9位就可以随意了。
# text = "18677889900"
# ret = re.match('''
# 1       #匹配第一位 为1
# [34587] #第二位为 3.4.5.8.7中的一个
# \d{9}   #匹配剩下的9个要求为数字
# ''',text, re.VERBOSE)
# print(ret.group())


# 2. 验证邮箱：邮箱的规则是邮箱名称是用数字、英文字符、下划线组成的，然后是@符号，后面就是域名了。
# text = "hynever@163.com"
# ret = re.match('\w+@[a-z0-9]+\.[a-z]+', text)
# ret = re.match('''
# \w+         #前几位能是数字 英语 和下划线
# @           #匹配@
# [a-z0-9]+   # 匹配a-z 0-9到.之前
# \.          #匹配.
# [a-z]+      #最后都是小写
# ''',text, re.VERBOSE)
# print(ret.group())


# 3. 验证URL：URL的规则是前面是http或者https或者是ftp然后再加上一个冒号，再加上一个斜杠，再后面就是可以出现任意非空白字符了。
text = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
ret = re.match('(http|https|ftp)://\S+',text)
print(ret.group())


# 4. 验证身份证：身份证的规则是，总共有18位，前面17位都是数字，后面一位可以是数字，也可以是小写的x，也可以是大写的X。
# text = "36530019870716234x"
# ret = re.match('\d{17}[0-9Xx]', text)
# print(ret.group())