class NGL:
    def __init__(self):
        self.stack = []
        self.res = []

    def next(self, nums):
        for i in nums:
            if len(self.stack) == 0:
                self.stack.append(i)
                self.res.append(-1)
            else:
                flag = True
                while self.stack:
                    if self.stack[-1] > i:
                        self.res.append(self.stack[-1])
                        self.stack.append(i)
                        flag = False
                        break
                    self.stack.pop()
                if flag:
                    self.res.append(-1)
                    self.res.append(i)
        return self.res


obj = NGL()
res = obj.next([100, 80, 60, 70, 60, 75, 85])
print(res)
