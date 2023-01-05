class A:
    def __init__(self, name:str, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "吃")


a = A("1", 2)
print(a.name)
a.eat()
