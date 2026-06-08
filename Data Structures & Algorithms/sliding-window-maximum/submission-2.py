class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # check max in widnow constantly
        # keep pointer to max, only refresh when needed
        # max heap, with index
        
        result = []
        max_heap = [] # (-value, index)

        left = 0
        for i in range(k - 1):
            heapq.heappush(max_heap, (-nums[i], i))
        
        for r in range(k - 1, len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))
            flipped_max, index = max_heap[0]
            while index < r - k + 1:
                flipped_max, index = heapq.heappop(max_heap)
            result.append(-flipped_max)
            heapq.heappush(max_heap, (flipped_max, index))
        return result

            
        
