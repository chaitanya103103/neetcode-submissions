class MinStack:

    def __init__(self):
        self.s = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.s.append(val)

        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val,self.minstack[-1]))


    def pop(self) -> None:
        self.s.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
