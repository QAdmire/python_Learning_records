# -*- coding: UTF-8 -*-
def yy_yield(n):
    print("start")
    while n > 0:
        print("before")
        yield n     #yield与return的区别 yield 会暂时挂起，等待下一次的执行， return是直接退出
        n -= 1
        print("after")
def fibs():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

import itertools
# a = fibs()
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

print(list(itertools.islice(fibs(),10)))
