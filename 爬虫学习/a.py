import re
text = 'https://tieba.baidu.com/mo/q/posts?tid=7322645181&pid=139023585937#/'
result =  re.match('.+?tid=(.+?)&',text)
print(result.group(1))