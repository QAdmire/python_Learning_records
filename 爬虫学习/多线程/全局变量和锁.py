# -*- coding: UTF-8 -*-
import threading


v = 0
glock = threading.Lock()

#lock的原则，把尽量少和耗时短的代码放在锁中
#记得释放锁
#为什么要用锁 因为线程执行的顺序是无序的。有可能会造成数据错误
#修改全局变量才用

class Test(threading.Thread):
    def run(self) -> None:
        global v
        glock.acquire() #上锁
        for x in range(1000000):
            v += 1
        glock.release() #解锁
        print(v)


def main():
    for x in range(2):
        t = Test()
        t.start()



if __name__ == '__main__':
    main()