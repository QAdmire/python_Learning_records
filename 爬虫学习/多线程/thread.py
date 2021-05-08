# -*- coding: UTF-8 -*-
import threading
import time


def coding():
    for x in range(3):
        print("{}正在写代码".format(x))
        time.sleep(1)


def drawing():
    for x in range(3):
        print("{}正在写画画".format(x))
        time.sleep(1)


def single_thread():
    start = time.time()
    # 单线程
    coding()
    drawing()

    end = time.time()

    print(end - start)


def multi_thread():

    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()


if __name__ == "__main__":
    single_thread()

    multi_thread()
