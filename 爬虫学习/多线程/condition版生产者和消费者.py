# -*- coding: UTF-8 -*-
import threading
import random
import time

gMoney = 0
gCondition = threading.Condition()
gTimes = 0


class Producer(threading.Thread):
    def run(self) -> None:
        global gMoney
        global gTimes

        while True:
            money = random.randint(0, 100)
            gCondition.acquire()
            gTimes += 1
            gMoney += money
            if gTimes >= 10:
                gCondition.release()

                break
            print("%s生产了%d元"%(threading.current_thread().name, money))
            gCondition.notify_all()
            # 如果不通知就会一直卡在等待处 举个例子
            # 消费者3号消费不够，然后后面救不会在出现，并且生产者已经不再生产了！并且会卡死
            # 如果通知 最后消费者应该都有一条 生产者已经不再生产了
            gCondition.release()
            time.sleep(1)


class Cunsumer(threading.Thread):
    def run(self) -> None:
        global gMoney
        global gTimes
        while True:
            money = random.randint(0, 100)
            gCondition.acquire()
            while gMoney < money:
                if gTimes >= 10:
                    print("%s想消费%d元钱，但是余额只有%d元钱了，并且生产者已经不再生产了！" % (threading.current_thread().name, money, gMoney))
                    gCondition.release()
                    return
                print("%s想消费%d元钱，但是余额只有%d元钱了，消费失败！"%(threading.current_thread().name,money,gMoney))
                gCondition.wait()
            gMoney -= money
            print("%s消费了%d元钱，剩余%d元钱" % (threading.current_thread().name, money, gMoney))
            gCondition.release()
            time.sleep(1)


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