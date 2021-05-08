# -*- coding: UTF-8 -*-
import threading
import random
import time

gMoney = 0
gLock = threading.Lock()
gTimes = 0


class Producer(threading.Thread):
    def run(self) -> None:
        global gMoney
        global gTimes

        while True:
            money = random.randint(0, 100)
            gLock.acquire()
            gTimes += 1
            gMoney += money
            if gTimes >= 10:
                gLock.release()

                break
            print("%s生产了%d元"%(threading.current_thread().name, money))

            gLock.release()



class Cunsumer(threading.Thread):
    def run(self) -> None:
        global gMoney
        global gTimes
        while True:
            money = random.randint(0, 100)
            gLock.acquire()
            if gMoney>=money:
                gMoney -= money
                print("%s消费了%d元,剩余%d元" % (threading.current_thread().name, money, gMoney))
            else:
                if gTimes >= 10:
                    gLock.release()
                    break
                print("钱不够")

            gLock.release()



def main():
    for x in range(5):
        th = Producer(name='生产者%d'%x)
        th.start()

    for x in range(5):
        th = Cunsumer(name='消费者%d'%x)
        th.start()

    print(gMoney)

if __name__ == '__main__':
    main()