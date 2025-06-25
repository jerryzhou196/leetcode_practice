class MinStack:
    def __init__(self):
        self.stack = []
        self.smallest = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.smallest:
            if val < self.smallest[-1]:
                self.smallest.append(val)
            else:
                self.smallest.append(self.smallest[-1])
        else:
            self.smallest.append(val)

    def pop(self) -> None:
        self.smallest.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()