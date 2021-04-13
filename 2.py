# coding : UTF-8
"""
得到每个单词的字母数量
"""
s = "Life1is55short~You2 !need python"
linshi = []
b = []
"""
for i in s:
    if i.isalpha():
        linshi.append(i)
        t = 1
    else:
        if t == 1:
            b.append("".join(linshi))
        t = 0
        linshi = []

print(b)
个人str.split()函数实现方法
"""
d = s.split(" ")
c = {}
for els in d:
    for i in els:
        if c.get(els) is None:
            c[els] = 1
        else:
            c[els] += 1
print(c)
