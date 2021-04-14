from functools import wraps
'''
自定义显示分数
numerator 分子
denominator 分母
加入了约分
'''

def gcd(x,y):
    if x%y == 0:
        return y
    else:
        return gcd(y, x%y)

class Fraction:
    def __init__(self, numerator , denominator  = 1):
        n = gcd(numerator,denominator)
        print(n)
        self.numerator  = int(numerator/n)
        self.denominator  = int(denominator/n)

    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)

    __repr__ = __str__

i =  Fraction(9,99)
print(i)
