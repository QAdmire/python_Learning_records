import itertools as its

a = its.product('abcd',repeat=3)
# 'abcd' 'abcd' 'abcd' repeat重复3次
for i in a:
    for j in i:
        a = "".join(i)
        print(a)



