class MaxStack:

    def __init__(self):
        self.stack = []
        self.deleted = set()
        self.count = 0
        self.heap = []

    def push(self, x: int) -> None:
        self.stack.append([x, self.count])
        heapq.heappush(self.heap, [-x, -self.count])
        self.count += 1
        

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.deleted:
            self.stack.pop()
        res, count = self.stack.pop()
        self.deleted.add(count)
        return res
        

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.deleted:
            self.stack.pop()
        return self.stack[-1][0]


    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.deleted:
            heapq.heappop(self.heap)
        
        return -self.heap[0][0]
        
    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.deleted:
            heapq.heappop(self.heap)
        
        val, count = heapq.heappop(self.heap)
        val = -val
        count = -count

        self.deleted.add(count)
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
