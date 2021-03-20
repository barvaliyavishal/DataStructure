class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        self.topmin = -1
        self.top = -1

    def minval(self,val):
        if self.topmin + 1 == len(self.min):
            if self.topmin >= 0 and self.min[self.topmin] >= val:
                self.min.append(val)
                self.topmin += 1
            elif self.topmin == -1:
                self.topmin += 1
                self.min.append(val)
        else:
            if self.topmin == -1:
                self.topmin += 1
                self.min[self.topmin] = val
            else:
                if self.min[self.topmin] >= val:
                    self.topmin += 1
                    self.stack[self.topmin] = val

    def push(self, x: int) -> None:
        if self.top+1 == len(self.stack):
            self.stack.append(x)
            self.top += 1
        else:
            self.top += 1
            self.stack[self.top] = x
        self.minval(x)

    def pop(self) -> None:
        if self.top >= 0:
            if self.stack[self.top] == self.min[self.topmin]:
                self.top -=1
                self.topmin -= 1
            else:
                self.top -= 1

    def topp(self):
        if self.top != -1:
            return self.stack[self.top]

    def getMin(self) -> int:
        if self.topmin != -1:
            return self.min[self.topmin]


obj = MinStack()
flag = True
while flag:
    inp = int(input("1 for push "
                    " 2 for pop "
                    "3 for get min "
                    "4 for top 5 for exit " ))
    if inp == 1:
        obj.push(int(input("enter value to push")))
    elif inp == 2:
        print(obj.pop())
    elif inp == 3:
        print(obj.getMin())
    elif inp == 4:
        print(obj.topp())
    else:
        flag = False
    print(obj.stack)
    print(obj.min)
