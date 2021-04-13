import datetime

"""
凯撒密码加密实现方法 字典匹配
速度比一个一个处理快
"""
start = datetime.datetime.now()
password = open("random.txt", "r+")
kaisha = password.read()
password.close()
key = 1
dict_a_z = dict()
for i in range(65, 91):
    dict_a_z.update(dict.fromkeys(chr(i), chr(i)))
for i in range(65, 91):
    if i + key > 90:

        dict_a_z[chr(i)] = chr(i + key - 90 + 64)
    else:
        dict_a_z[chr(i)] = chr(i + key)
kaisha_lsit = list(kaisha)
new_password = list()

for i in range(len(kaisha)):
    new_password.append(dict_a_z.get(kaisha_lsit[i]))
end = datetime.datetime.now()
print(end - start)
