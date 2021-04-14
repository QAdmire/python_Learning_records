#coding:utf-8
'''
物理学家 继承 理论物理学家 和 实验物理学家
'''

class physicist:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class lilun_physicist(physicist):
    def __init__(self, chenjiu, name, age):
        self.chenjiu = chenjiu
        super().__init__(name, age)

class shiyan_physicist(physicist):
    def __init__(self, chenjiu, name, age):
        self.chenjiu = chenjiu
        super().__init__(name, age)
