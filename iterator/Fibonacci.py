#coding:utf-8
import itertools
class Fibs:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration()
        self.a, self.b = self.b, self.a + self.b
        #类似 a,b = a+b,b-a 是先计算右边 然后再进行赋值
        # a = self.b
        # b = self.a + self.b
        # self.a = a
        # self.b = b



        #F(N) = F(N-1) + F(N-2)
        #此处是self.a+self.b self.a的值未变 故新的b是原来的a+加原来的b 可理解为上上一项的a 加上一项的b 等于新b
        #
        return fib
coule = itertools.count(start=1) #表示从1到无限的数

print(next(coule))
print(next(coule))
print(next(coule))
print([i for i in Fibs(5)])
fib = Fibs(100000)
print(list(itertools.islice(fib,10)))
