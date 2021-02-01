class Stack:
    def __init__(self):
        self.arr = []
        self.top = -1
        self.min = None

    def push(self, val):
        self.top+=1
        if self.top < len(self.arr):
            self.arr[self.top] = 