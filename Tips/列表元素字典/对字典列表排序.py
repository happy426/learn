dict1 = [
    {"name": "James",
     "num": 25},
    {"name": "Alice",
     "num": 39},
    {"name": "Hoton",
     "num": 35}
]

# 方法1 利用字典的sort函数
dict1.sort(key=lambda item: item["num"])
print(dict1)

# 方法2 利用sorted函数
dict1 = sorted(dict1, key=lambda item: item["num"])
print(dict1)

l = [1, 2, 3, 4, 5]
print(sorted(l, reverse=True))
l.sort()
print(l)
