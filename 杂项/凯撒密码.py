import datetime

start = datetime.datetime.now()
# password = input("输入你的原始密码：")
# kasha = int(input("加密值："))
new_password = []
fo = open("random.txt", "r+")
password = fo.read()

fo.close()
kasha = 1

for i in range(len(password)):
    if password[i] <= "Z" and password[i] >= "A":
        x = ord(password[i]) + kasha % 26

        if x > ord("Z"):
            new_password.append(chr(x - ord("Z") + 64))
        else:
            new_password.append(chr(x))

endtime = datetime.datetime.now()
print(endtime - start)
