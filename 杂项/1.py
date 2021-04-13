# coding : UTF-8
import random, math

lst = []
for i in range(100):
    lst.append(random.randint(1, 10))

dic = {}
for i in lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 0
print(dic)
