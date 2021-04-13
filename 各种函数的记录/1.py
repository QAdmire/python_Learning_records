import itertools as its

words = 'abcdefghijklmnopqrstuvwxyz1234567890'

r = its.product(words, repeat=2)  # repeat 要生成多少位的字典

dic = open("passda.txt", "a")
for i in r:
    dic.write("".join(i))
    dic.write("".join("\r"))
dic.close()