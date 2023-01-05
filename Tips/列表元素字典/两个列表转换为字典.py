list1 = ['James', 'Alice', 'Hoton']
list2 = [88, 86, 91]

# 方法1 利用zip内置函数
dict1 = dict(zip(list1, list2))

# 方法2 去除dict的隐式转换
dict2 = {key: value for key, value in zip(list1, list2)}

# 方法3 利用for循环
dict3 = {}
for k, v in zip(list1, list2):
    if k not in dict3.keys():
        dict3[k] = v

print("dict1:", dict1)
print("dict2:", dict2)
print("dict3:", dict3)

for i in zip(list1, list2):
    print(i)
    print(i[0])
    print(type(i))
