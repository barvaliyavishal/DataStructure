class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size, self.limit = 0, maxSize


    def push(self, x: int) -> None:
        if self.size==self.limit:
            return
        self.stack.append([x, 0])
        self.size+=1

    def pop(self) -> int:
        if self.size==0:
            return -1

        popped, increment = self.stack.pop()
        self.size-=1
        if self.size:
            self.stack[-1][1] +=increment

        return popped+increment

    def increment(self, k: int, val: int) -> None:

        k = min(self.size, k)
        if k:
            self.stack[k-1][1] +=val