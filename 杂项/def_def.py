a = 1
def func():
    print(a+1)


func()

def func1():
    global a
    a = a + 1
    print(a)
func1()

def func2():
    c = 1
    def func3():
        nonlocal c
        c = c + 1
        print(c)
    return func3()
ac = func2()
def weight(g):
    def G(m):
        return m*g
    return G
W = weight(10)
MG = W(100)
print(MG)