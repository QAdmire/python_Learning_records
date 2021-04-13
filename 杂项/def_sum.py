def add(*x):
    sum1 = 0
    print(x)
    for i in range(len(x)):
        sum1 += x[i]
    return print(sum1)


add(1, 2, 5, 3, 5)
