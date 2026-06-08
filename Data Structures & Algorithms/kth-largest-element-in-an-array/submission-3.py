class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # keep k largest values, so if smallest value is less than num, pop and push
        
        for num in nums:
            if len(heap) == k and heap[0] < num:
                heapq.heappop(heap)
            if len(heap) < k:
                heapq.heappush(heap, num)
        return heapq.heappop(heap)