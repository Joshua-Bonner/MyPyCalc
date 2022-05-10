def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return f'{x / y:.2f}'


def pow(x, y):
    temp = 1
    cnt = y
    while cnt != 0:
        temp *= x
        cnt -= 1
    return temp


def sqrt(x):
    return


class MyCalculator:
    x: float
    y: float
    operation: str

    def __init__(self):
        print('Calculator Online!!!')
        operation = None
