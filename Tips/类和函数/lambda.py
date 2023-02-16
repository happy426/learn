def func(num):
    return lambda x: x * num


if __name__ == '__main__':
    result1 = func(10)
    print(result1(9))

    a = lambda x: x**2
    print(a(9))
    print((lambda x, y: x ** y)(2, 3))

    a = [{'name': 'B', 'age': 50}, {'name': 'A', 'age': 30}, {'name': 'C', 'age': 40}]
    print(sorted(a, key=lambda x: x['name']))  # 按姓名排序
    print(sorted(a, key=lambda x: x['age']))  # 按年龄排序
