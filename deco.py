def p_deco(x):
    def wrapper(name):
        return '<p>{0}</p>'.format(x(name))
    return wrapper

@p_deco
def book(nam1e):
    return "the name of my book is {0}".format(nam1e)

py_book = book("BBBB")
print(py_book)
