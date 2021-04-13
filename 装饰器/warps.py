import time


def timethis(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        return end - start
    return wrapper

@timethis
def cont():
    lst = []
    for i in range(100000):
        lst.append(i)

a = cont()
print(a)
