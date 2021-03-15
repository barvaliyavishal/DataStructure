class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min == None:
            self.min = x
        else:
            self.min = min(x, self.min)

    def pop(self) -> None:
        element = self.stack.pop()
        if not self.stack:
            self.min = None
        if element == self.min:
            self.min = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

obj = MinStack()
obj.push(10)
obj.push(4)
obj.push(9)
obj.push(9)
obj.push(1)
obj.push(1)
print(obj.top())

obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
print(obj.getMin())
