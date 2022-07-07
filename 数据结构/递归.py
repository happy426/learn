"""
递归的特点：
调用自身
结束条件
"""


def fun(x):
    if x > 0:
        print(x)
        fun(x-1)
    else:
        print(0)
        return 0


if __name__ == '__main__':
    fun(9)
