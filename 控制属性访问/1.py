# -*- coding: UTF-8 -*-
class g:
    def __getattr__(self, item):
        print("nnn")
    def __setattr__(self, key, value):
        print("111")
        self.__dict__[key] = value
a = g()
print(a.a)

a.x = 1
print(a.x)