class MinStack:

    def __init__(self):
        self.stack=[]
        self.min=[]
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min:
            self.min.append(min(self.min[-1],value))
        else:
            self.min.append(value)
    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()