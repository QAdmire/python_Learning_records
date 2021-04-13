import random

lst = []
for i in range(9999999):
    random1 = random.randrange(65, 91)
    lst.append(chr(random1))
a = "".join(lst)
fo = open("random.txt", "w")
fo.write(a)
fo.close()
