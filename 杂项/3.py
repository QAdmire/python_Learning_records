# coding:UTF-8
import random

answer = random.randint(1, 100)
s = 0
while s != answer:
    s = int(input("you answer :\n"))
    if s > answer:
        print("NO,YOU INPUT IS BIG")
        continue
    elif s < answer:
        print("NO,YOU INPUT IS SMALL")
        continue
    else:
        print("LUCK,YOU !")
        break
