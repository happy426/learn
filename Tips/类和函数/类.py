class A:
    x = 5


class Person:
    """
    self 参数是对类的当前实例的引用，用于访问属于该类的变量。
    它不必被命名为 self，您可以随意调用它，但它必须是类中任意函数的首个参数：
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"hello, my name is {self.name},and I'm {self.age} years old!")


class Student(Person):
    """
    当添加 __init__() 函数时，子类将不再继承父的 __init__() 函数。

    注释：子的 __init__() 函数会覆盖对父的 __init__() 函数的继承。

    如需保持父的 __init__() 函数的继承，请添加对父的 __init__() 函数的调用：
    """
    def __init__(self, s_name, s_age, cla="一年级"):
        Person.__init__(self, s_name, s_age)
        self.cla = cla

    def eat(self):
        print(f'我{self.name}一顿干2碗大米饭')


if __name__ == '__main__':
    a = A
    print(a.x)
    zhangSan = Person("张三", "18")
    print(zhangSan.name + zhangSan.age)
    zhangSan.say_hello()  # 调用函数

    xiaoMing = Student('小明', '8')
    print(xiaoMing.name+xiaoMing.cla)
    xiaoMing.say_hello()
    xiaoMing.eat()
