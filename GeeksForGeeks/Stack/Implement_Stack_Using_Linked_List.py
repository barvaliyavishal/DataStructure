class Node:
    def __init__(self,val):
        self.data = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        temp = None
        if self.head:
            temp = self.head.data
            self.head = self.head.next
        return temp

    def top(self):
        if self.head:
            return self.head.data
        else:
            return None

    def isEmpty(self):
        if self.head:
            return False
        else:
            return True

    def show(self):
        temp = self.head
        while temp:
            print(temp.data, " -> ", end="")
            temp = temp.next


stack = Stack()
flag = True
while flag:
    res = int(input("1 for push   2 for pop   3 for esEmpty   4 for TOp else for exit"))
    if res == 1:
        stack.push(int(input("Enter Value to Push : ")))
    elif res == 2:
        print(stack.pop())
    elif res == 3:
        print(stack.isEmpty())
    elif res == 4:
        print(stack.top())
    else:
        flag = False
