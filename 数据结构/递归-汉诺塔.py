def Hn(n, a, b, c):
    """
    :param n:层数
    :param a: a柱
    :param b:
    :param c:
    :return: 步骤
    """
    if n == 1:
        print(a, '->', c)
    else:
        Hn(n-1, a,b,c)
        print(a, '->', c)
        Hn(n-1,b, a ,c)


n = int(input())
Hn(n, "a", "b", "c")

