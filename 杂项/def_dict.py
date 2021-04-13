def dict_c(dct, **kwargs):
    for k, v in kwargs.items():
        if dct.get(k) == v:
            print({k: v})
        else:
            print("no")


d = {"a": 39, "b": 40, "c": 99, "d": 100}
dict_c(d, a=39, b=3)
