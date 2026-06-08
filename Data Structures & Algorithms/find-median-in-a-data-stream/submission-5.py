class MedianFinder:

    def __init__(self):
        self.maxLeft = []
        self.minRight = []
        

    def addNum(self, num: int) -> None:
        if not self.minRight or self.minRight[0] <= num:
            heapq.heappush(self.minRight, num)
        else:
            heapq.heappush(self.maxLeft, -num)
        
        # rebalance if difference is bigger than 1

        while len(self.maxLeft) < len(self.minRight):
            right_min = heapq.heappop(self.minRight)
            heapq.heappush(self.maxLeft, -right_min)
        
        while len(self.maxLeft) > len(self.minRight):
            left_max = -heapq.heappop(self.maxLeft)
            heapq.heappush(self.minRight, left_max)

    
    def findMedian(self) -> float:
        left_len = len(self.maxLeft)
        right_len = len(self.minRight)
        if (left_len + right_len) % 2 == 0:
            return (-self.maxLeft[0] + self.minRight[0]) / 2
        
        if left_len > right_len:
            return -self.maxLeft[0]
        else:
            return self.minRight[0]
            
    
        
        