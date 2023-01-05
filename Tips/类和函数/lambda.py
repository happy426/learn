def func(num):
    return lambda x: x * num


if __name__ == '__main__':
    result1 = func(10)
    print(result1(9))

    a = lambda x: x**2
    print(a(9))