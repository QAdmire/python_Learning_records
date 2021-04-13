import time
from functools import wraps



def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(func.__name__,end - start)
    return wrapper

@timethis
def cont():
    lst = []
    for i in range(100000):
        lst.append(i)
@timethis
def cc(n):
    while n>0:
        n-=1
a = cont()
cc(1000000)
