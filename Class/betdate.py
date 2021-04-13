# coding:utf-8
import datetime
from dateutil import rrule


class Betdate:
    def __init__(self, start_time, end_time):
        self.start = datetime.datetime.strptime(start_time, "%Y, %m, %d")
        self.end = datetime.datetime.strptime(end_time, "%Y, %m, %d")

    def days(self):
        d = self.end - self.start
        return d.days if d.days > 0 else False

    def weeks(self):
        weeks = rrule.rrule(rrule.WEEKLY, dtstart=self.start, until=self.end)
        return weeks.count()


Date = Betdate("2021, 3, 22", "2022, 3, 12")
Date.start = datetime.datetime.today() #实例属性的修改
print(Date.__dict__) #打印实例属性
d = Date.days()
w = Date.weeks()
print(d,w)