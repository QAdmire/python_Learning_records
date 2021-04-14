#coding:utf-8
class Time_examine:
    def __init__(self,year,month,day): #初始化方法
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls,date_as_string):
        year, month , day = map(int, date_as_string.split('-'))
        date1 = cls (year, month, day )    #（实例化方法）classmethod类方法调用类 目前能知道的作用是 如果类改名了还是可以通过这样调用
        return date1                       #等同于 Time_examine(year,month,day)

    @staticmethod
    def is_date_check(date_as_string):    #静态方法 目前知道是用于 这个方法和实例无关用
        year, month, day = map(int, date_as_string.split('-'))
        return day <= 31 and year <= 2038 and month <= 12
    # def time_check(self):
    #     if self.year < 0 or self.year > 9999:
    #         return False
    #     elif self.month in [1,3,5,7,8,10,12]:
    #         if self.day > 0 and self.day <=31:
    #             return True
    #     elif self.month in [4,6,9,11]:
    #         if self.day > 0 and self.day <=30:
    #             return True
    #     elif self.month == 2:
    #         if self.day > 0 and self.day <= 28:
    #             return True
    #     else:
    #         return False
d = Time_examine(1999,6,2)
d1 = Time_examine.from_string("1999-6-2")
d2 = Time_examine.is_date_check("1999-30-15")
print(d,d1,d2)


