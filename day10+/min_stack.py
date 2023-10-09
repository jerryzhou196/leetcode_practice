class MinStack:
    def __init__(self):
        self.data = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.data[len(self.data) - 1].append(val)

        if len(self.min_stack) == 0:
            self.min_stack.append(val)

        if val < self.min_stack[len(self.min_stack) - 1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[len(self.min_stack) - 1])

    def pop(self) -> None:
        self.min_stack.pop()

    def top(self) -> int:
        return self.data[len(self.data) - 1]

    def getMin(self) -> int:
        return self.min_stack[len(self.min_stack) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
