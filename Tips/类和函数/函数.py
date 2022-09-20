"""
函数声明中，text:str
text 是参数 :冒号后面  str是参数的注释。
如果参数有默认值，还要给注释，如下写。
max_len:'int>0'=80

->str 是函数返回值的注释。

这些注释信息都是函数的元信息，保存在f.__annotations__字典中、

需要注意，python对注释信息和f.__annotations__的一致性，不做检查
不做检查，不做强制，不做验证！什么都不做。
"""


def say(name: str, age: int) -> str:
    res = f"{name}今年{age}岁，'并且giao!了一声'"
    return res


if __name__ == '__main__':
    s = say('小啊giao~', 18)
    print(s)
