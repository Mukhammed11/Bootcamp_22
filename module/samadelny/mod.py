def ariif(x: int ):
    return x ** 2


# print(ariif())

def num(x: int ):
    return x ** 3


# print(num(2))

def p(a: int, b: int):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Not a number'


# print(p(10, 0))


def i(a: int, b: int):
    return a * b


# print(i(6, 10))


def k(x: int, s: int):
    return x % s

# print(k(10, 25))