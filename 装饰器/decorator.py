import time


def timeit(num):

    def inner(f):

        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(num):
                ret = f(*args, **kwargs)
            print(time.time() - start)
            return ret

        return wrapper

    return inner


@timeit(2)
def my_func(x):
    time.sleep(x)

# 执行1000次
@timeit(1000)
def add_func(x, y):
    return x + y


if __name__ == '__main__':
    my_func(2)
    print(add_func(2, 3))

