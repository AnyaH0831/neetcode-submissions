class MinStack:

    def __init__(self):
        self.stack = []
        self.prefixMin = []

    def push(self, val: int) -> None:
        self.stack += [val]

        if len(self.prefixMin) > 0:
            if self.prefixMin[-1] > val:
                self.prefixMin += [val]
            else:
                self.prefixMin += [self.prefixMin[-1]]
        else:
            self.prefixMin += [val]
        # print(self.prefixMin)
        # print(self.stack)

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.prefixMin = self.prefixMin[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefixMin[-1]
        
