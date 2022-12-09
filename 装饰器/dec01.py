def dec(f):
    print("使用装饰器")


def double(x):
    return x * 2

@dec
def triple(x):
    return x * 3


def calc_number(func, x):
    print(func(x))


if __name__ == '__main__':
    calc_number(double, 10)
    dec(double)