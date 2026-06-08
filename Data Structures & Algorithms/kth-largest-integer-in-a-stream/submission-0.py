class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # [3, 3, 2]
        # min heap only holding at most k values
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
