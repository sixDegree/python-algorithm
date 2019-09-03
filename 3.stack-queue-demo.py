
# 1. Stack: 先进后出(可用顺序表或链表实现)
class Stack:
    def __init__(self):
        self.__items=[]
    
    def push(self,item):
        self.__items.append(item)   # 尾部插入
        return item

    def pop(self):
        return self.__items.pop()   # 尾部弹出

    def is_empty(self):
        return len(self.__items)==0

    def size(self):
        return len(self.__items)


def test_stack():
    print("Test Stack:")
    s=Stack()
    print("is_empty:",s.is_empty())
    print("push:",s.push('A'))
    print("push:",s.push('B'))
    print("push:",s.push('C'))
    print("size:",s.size())
    print("pop:",s.pop())
    print("pop:",s.pop())
    print("pop:",s.pop())
    print("size:",s.size())


# 2. Queue: 先进先出(可用顺序表或链表实现)

class Queue:

    def __init__(self):
        self.__items=[]
    
    def push(self,item):
        self.__items.append(item)       # 尾部插入
        return item

    def pop(self):
        return self.__items.pop(0)      # 头部弹出

    def is_empty(self):
        return len(self.__items)==0

    def size(self):
        return len(self.__items)


def test_queue():
    print("Test Queue:")
    q=Queue()
    print("is_empty:",q.is_empty())
    print("push:",q.push('A'))
    print("push:",q.push('B'))
    print("push:",q.push('C'))
    print("size:",q.size())
    print("pop:",q.pop())
    print("pop:",q.pop())
    print("pop:",q.pop())
    print("size:",q.size())


if __name__ == '__main__':

    test_stack()
    print("***"*10)

    test_queue()
    print("***"*10)

