class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.m = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.m is None:
            self.m = x

        if x < self.m:
            tmp = x
            x = 2 * x - self.m
            self.m = tmp

        self.s.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.s[-1] < self.m:
            self.m = 2 * self.m - self.s[-1]
        self.s = self.s[:-1]
        if not self.s:
            self.m = None

    def top(self):
        """
        :rtype: int
        """
        if self.s[-1] < self.m:
            return self.m
        else:
            return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.m