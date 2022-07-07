def jie(n):
    if n == 1:
        return 1
    else:
        return n*jie(n-1)


num = 0
for i in range(1,21):
    print(i)
    num = num + jie(i)
print(num)
print(jie(1),jie(3), jie(4))