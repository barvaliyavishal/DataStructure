class ThreeInOne:
    def __init__(self, size):
        self.stack = [-1]*size
        self.start = [-1]*3
        self.end = [-1]*3
        self.maintop = 0
        self.size = size

    def shift_right(self, start_index, end_index):
        for i in range(end_index, start_index-1, -1):
            self.stack[i+1] = self.stack[i]

    def shift_left(self, start_index, end_index):
        for i in range(start_index,end_index+1):
            self.stack[i-1] = self.stack[i]

    def push(self, sn, val):
        if self.maintop >= self.size:
            print("Stack Overflow")
            return

        if sn == 0:
            if self.start[1] == -1 and self.start[2] == -1:
                if self.start[0] == -1:
                    self.start[0] = self.maintop
                    self.end[0] = self.maintop
                    self.stack[self.maintop] = val
                    self.maintop += 1
                else:
                    self.end[0] = self.maintop
                    self.stack[self.maintop] = val
                    self.maintop += 1
            elif self.start[1] != -1 and self.start[2] != -1:
                self.shift_right(self.start[1], self.end[2])
                self.stack[self.start[1]] = val
                if self.start[0] == -1:
                    self.end[0] = self.start[0] = self.start[1]
                else:
                    self.end[0] += 1
                self.start[1] += 1
                self.start[2] += 1
                self.end[1] += 1
                self.end[2] += 1
                self.maintop += 1
            elif self.start[1] != -1 and self.start[2] == -1:
                self.shift_right(self.start[1], self.end[1])
                self.stack[self.start[1]] = val
                if self.start[0] == -1:
                    self.end[0] = self.start[0] = self.start[1]
                else:
                    self.end[0] += 1
                self.start[1] += 1
                self.end[1] += 1
                self.maintop += 1
            elif self.start[2] != -1 and self.start[1] == -1:
                self.shift_right(self.start[2], self.end[2])
                self.stack[self.start[2]] = val
                if self.start[0] == -1:
                    self.end[0] = self.start[0] = self.start[2]
                else:
                    self.end[0] += 1
                self.start[2] += 1
                self.end[2] += 1
                self.maintop += 1

        elif sn == 1:
            if self.start[2] == -1:
                self.stack[self.maintop] = val
                if self.start[1] == -1:
                    self.start[1] = self.end[1] = self.maintop
                else:
                    self.end[1] += 1
                self.maintop += 1

            else:
                self.shift_right(self.start[2], self.end[2])
                self.stack[self.start[2]] = val
                if self.start[1] == -1:
                    self.start[1] = self.end[1] = self.start[2]
                else:
                    self.end[1] += 1
                self.start[2]+=1
                self.end[2] += 1
                self.maintop +=1
        elif sn == 2:
            self.stack[self.maintop] = val
            if self.start[2] == -1:
                self.start[2] = self.end[2] = self.maintop
            else:
                self.end[2] += 1
            self.maintop += 1

        else:
            print("Enter Valid Stack Number")

    def pop(self,sn):
        if self.start[sn] == -1:
            print("Stack Is Empty")
            return
        else:
            res = self.stack[self.end[sn]]
            if sn == 0:
                if self.start[1] != -1 and self.start[2] != -1:
                    self.shift_left(self.start[1], self.end[2])
                    self.start[1] -= 1
                    self.start[2] -= 1
                    self.end[1] -= 1
                    self.end[2] -= 1
                    self.maintop -= 1
                    if self.start[0] == self.end[0]:
                        self.start[0] = self.end[0] = -1
                    else:
                        self.end[0] -= 1

                elif self.start[1] != -1:
                    self.shift_left(self.start[1],self.end[1])
                    self.start[1] -= 1
                    self.end[1] -= 1
                    self.maintop -= 1
                    if self.start[0] == self.end[0]:
                        self.start[0] = self.end[0] = -1
                    else:
                        self.end[0] -= 1
                elif self.start[2] != -1:
                    self.shift_left(self.start[2], self.end[2])
                    self.start[2] -= 1
                    self.end[2] -= 1
                    self.maintop -= 1
                    if self.start[0] == self.end[0]:
                        self.start[0] = self.end[0] = -1
                    else:
                        self.end[0] -= 1
                elif self.start[1] == -1 and self.start[2] == -1:
                    self.maintop -= 1
                    if self.start[0] == self.end[0]:
                        self.start[0] = self.end[0] = -1
                    else:
                        self.end[0] -= 1

            elif sn == 1:
                if self.start[2] == -1:
                    self.maintop -= 1
                    if self.start[1] == self.end[1]:
                        self.start[1] = self.end[1] = -1
                    else:
                        self.end[1] -= 1
                else:
                    self.shift_left(self.start[2], self.end[2])
                    self.start[2] -= 1
                    self.end[2] -= 1
                    self.maintop -= 1
                    if self.start[1] == self.end[1]:
                        self.start[1] = self.end[1] = -1
                    else:
                        self.end[1] -= 1

            elif sn == 2:
                if self.start[2] == self.end[2]:
                    self.start[2] = self.end[2] = -1
                else:
                    self.end[2] -= 1
            return res

    def top(self, sn):
        return self.stack[self.end[sn]]

obj = ThreeInOne(10)
flag = True
while flag:
    n = input("want more?  : ")
    if n != 'y':
        flag = False
    p = input("1 for push 2 for pop else for top")
    if p == '1':
        obj.push(int(input("stack Number : ")), int(input("val : ")))
    elif p == '2':
        res = obj.pop(int(input("Enter Stack number to pop")))
        print(res)
    else:
        res = obj.top(int(input("enter stack number for top : ")))
        print(res)


