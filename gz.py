time1 = ["1:19", "1:12", "1:10", "1:07", "1:02", "1:00", "0:53"]
time2 = []
c = []
h = int(input("输入h"))
for i in range(7):

    lst = time1[i].split(":")
    time2.append(int(lst[0]) * 60 + int(lst[1]) - h)

print(time1)
2
for i in range(7):
    a = str(int(time2[i]) % 60)
    b = str(int(int(time2[i]) / 60))
    c.append(b + ":" + a)

print(c)
