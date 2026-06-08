class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # keep k largest values, so if smallest value is less than num, pop and push
    
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
                
        return heapq.heappop(heap)