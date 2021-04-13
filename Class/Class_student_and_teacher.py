class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def do_work(self, time):
        if time > 3 and self.grade > 3:
            return True
        elif time > 0.5 and self.grade < 3:
            return True
        else:
            return False


class teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.x = 'sd'

    def evaluate(self, result=True):
        if result:
            return "GOOD!"
        else:
            return "BAD!"


zaolixin = Student("zaolixin", 4, "math")
liyiping = teacher("liyiping", "math")
liyiping_said = liyiping.evaluate(zaolixin.do_work(4))
print(
    "teacher {0} student {1} ,{2}".format(liyiping.name, zaolixin.name, liyiping_said)
)
print(dir(liyiping))
