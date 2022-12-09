"""
函数的返回值可以是函数
"""


def get_multiple_func(n):
    def multiple(x):
        return n * x

    return multiple


double = get_multiple_func(2)
triple = get_multiple_func(3)

print(double(10))
print(triple(20))
