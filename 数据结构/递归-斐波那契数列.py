def Fbo(x):
    """
    :param x: 输入的数列长度
    :return: 返回数列
    """

    if x <= 2:
        return 1
    else:
        return Fbo(x-1) + Fbo(x-2)


if __name__ == '__main__':
    n = int(input())
    print(Fbo(n))
    for i in range(1, n+1):
        print(Fbo(i), end=',')