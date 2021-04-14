from functools import wraps
import math
'''
自定义显示分数
numerator 分子
denominator 分母
加入了约分
'''

# def gcd(x,y):
#     if x%y == 0:
#         return y
#     else:
#         return gcd(y, x%y)

class Fraction:
    def __init__(self, numerator , denominator  = 1):
        n = math.gcd(numerator,denominator)
        self.numerator  = int(numerator/n)
        self.denominator  = int(denominator/n)

    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)

    __repr__ = __str__

    def __add__(self, other):
        print(other)
        if isinstance(other, (int, Fraction)):
#isinstance用来判断类型 isinstance(object, classinfo)
# object -- 实例对象。 classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                                    self.denominator * other.denominator) #官方文档实现方法

i =  Fraction(6,56)
b =  Fraction(5,2)
print(i+b)
