class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # [3, 3, 2]
        # min heap only holding at most k values
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)
       
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
