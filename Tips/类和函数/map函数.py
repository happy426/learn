a = [1, 2, 3]
for item in map(lambda x: x * x, a):
    print(item)

g = lambda x: x**2
for i in map(g, a):
    print(i)

for i in map(float, a):
    print(i)
