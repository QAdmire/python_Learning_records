# -*- coding: UTF-8 -*-
import threading
import time


# def coding():
#     the_thread = threading.current_thread()
#     print(the_thread.name)
#     for x in range(3):
#         print("{}正在写代码".format(x))
#         time.sleep(1)
#
#
# def drawing():
#     for x in range(3):
#         print("{}正在写画画".format(x))
#         time.sleep(1)
#
#
#
#
# def multi_thread():
#
#     t1 = threading.Thread(target=coding)
#     t2 = threading.Thread(target=drawing)
#
#     t1.start()
#     t2.start()
#
#
# if __name__ == "__main__":
#     multi_thread()

#继承

class CodingThreading(threading.Thread):
    def run(self) -> None:
        the_thread = threading.current_thread() #返回当前线程的对象
        print(the_thread.name)
        for x in range(3):
            print("{}正在写代码".format(the_thread.name))
            time.sleep(1)


class DrawingThreading(threading.Thread):
    def run(self) -> None:
        the_thread = threading.current_thread()
        for x in range(3):
            print("{}正在写画画".format(the_thread.name))
            time.sleep(1)


def multi_thread():
    t1 = CodingThreading()
    t2 = DrawingThreading()

    t1.start()
    t2.start()

if __name__ == '__main__':

    multi_thread()
    print(threading.enumerate()) #获取整个程序中的线程