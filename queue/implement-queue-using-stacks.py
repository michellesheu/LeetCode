class MyQueue:

    def __init__(self):
        self.p = []
        self.pp = []

    def push(self, x: int) -> None:
        self.p.append(x)
        
        
    def pop(self) -> int:
        # [1,2] -> [2,1]
        if not self.pp and self.p:
            while self.p:
                self.pp.append(self.p.pop())
        return self.pp.pop()



    def peek(self) -> int:
        if not self.pp and self.p:
            while self.p:
                self.pp.append(self.p.pop())
        return self.pp[-1]

    def empty(self) -> bool:
        return len(self.pp) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()