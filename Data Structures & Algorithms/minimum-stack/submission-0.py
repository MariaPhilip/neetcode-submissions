class MinStack:

    def __init__(self):
        self.stack = []
        self.count = -1
        self.minstack =[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            self.minstack.append(min(self.minstack[self.count],val))
        else:
            self.minstack.append(val)
        self.count +=1
        return
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minstack.pop()
            self.count-=1
        return

    def top(self) -> int:
        return self.stack[self.count]

    def getMin(self) -> int:
        return self.minstack[self.count]
        
