#coding:utf-8
class Myrange:
    def __init__(self, n):
        self.i = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

print("1",[i for i in Myrange(5)])