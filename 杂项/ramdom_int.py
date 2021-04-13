import random

"""
求100个随机1-10的出现次数


"""
dict_int = dict()

for i in range(10):
    dict_int[i + 1] = 0
    # dict_int.update(dict.fromkeys((i + 1,), 0)) dick.fromkey(可迭代对象，value)
for i in range(100):
    x = random.randint(1, 10)
    if x in dict_int:
        dict_int[x] += 1
    # else:
    #     dict_int.update(dict.fromkeys((x,),0))
    #     dict_int[x] = 1

print(dict_int)
