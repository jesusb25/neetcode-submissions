class MedianFinder:

    def __init__(self):
        # two heaps?
        self.heap1 = [] # max heap
        self.heap2 = [] # min heap
        
    
    def balance(self):
        while len(self.heap1) - len(self.heap2) > 1:
            num = heapq.heappop(self.heap1)
            heapq.heappush(self.heap2, -num)

        while len(self.heap2) - len(self.heap1) > 1:
            num = heapq.heappop(self.heap2)
            heapq.heappush(self.heap1, -num)


    def addNum(self, num: int) -> None:
        # add where appropiate based on 0 vals
        num1 = -self.heap1[0] if self.heap1 else -float('inf')

        if num1 > num:
            heapq.heappush(self.heap1, -num)
        else:
            heapq.heappush(self.heap2, num)
        
        self.balance()


        

    def findMedian(self) -> float:
        if len(self.heap1) == len(self.heap2):
            return (-self.heap1[0] + self.heap2[0]) / 2
        
        if len(self.heap1) > len(self.heap2):
            return -self.heap1[0]
        else:
            return self.heap2[0]
        
        