#coding:utf-8
'''
继承 人 学生
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class Student(Person):
    def __init__(self, school, name, age):
        self.school = school
        super().__init__(name, age)
    def grade(self,n):
        print("{0} {1}".format(self.name, str(n)))

student =  Student('ZHONGGUODAXUE', 'WANGDA', 28)
student.grade(99)
print(student.school)
print(student.get_age())
print(student.get_name())