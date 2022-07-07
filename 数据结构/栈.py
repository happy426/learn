class Stack(object):
    # 定义初始化方法：
    def __init__(self):
        self.__list = []

    # 压栈
    def push(self, item):
        self.__list.append(item)

    # 出栈
    def pop(self):
        return self.__list.pop()

    # 返回栈顶元素
    def peek(self):
        return self.__list[len(self.__list)-1]

    # 判断栈是否为空
    def is_empty(self):
        return self.__list == []

    # 返回栈的大小
    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    stack = Stack()
    print('是否空栈', stack.is_empty())
    # 压栈
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print('是否空栈', stack.is_empty())
    # 出栈
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print('是否空栈', stack.is_empty())



