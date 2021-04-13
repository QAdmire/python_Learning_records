# import hashlib
# f = open('superdic.txt','w')
# for i in range(10000000):
#     f.write("{0}\n".format(i))
# f.close()

import itertools as its

words = 'abcdefghijklmnopqrstuvwxyz1234567890'

r = its.product(words, repeat=6)  # repeat 要生成多少位的字典

dic = open("pass.txt", "a")
for i in r:
    dic.write("".join(i))
    dic.write("".join("\r"))
dic.close()