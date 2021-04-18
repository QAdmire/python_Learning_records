# -*- coding: UTF-8 -*-
while True:
    try:
        a = float(input("first number:"))
        b = float(input("second number:"))
        r = a / b
        print("{0} / {1} = {2}".format(a, b, r))
    except ZeroDivisionError:
        print("second can not zero")
    except ValueError:
        print("must be int")
    except:
        break
