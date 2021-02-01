class Stack:
    def __init__(self):
        self.arr = []
        self.top = -1

    def push(self, val):
        self.top += 1
        if self.top < len(self.arr):
            self.arr[self.top] = val
        else:
            self.arr.append(val)

    def pop(self):
        if self.top < 0:
            return "stack is Empty"
        self.top -= 1
        return self.arr[self.top+1]

    def peek(self):
        if self.top < 0:
            return "stack is Empty"
        return self.arr[self.top]

    def is_empty(self):
        if self.top == -1:
            return True
        return False


stack = Stack()
stack.push(5)
stack.push(6)
stack.push(7)
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.is_empty())
stack.pop()
print(stack.is_empty())
print(stack.peek())
