class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # check max in widnow constantly
        # keep pointer to max, only refresh when needed
        # max heap, with index
        
        result = []
        max_heap = [] # (-value, index)
        
        for r in range(len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))

            # evict elements outside the window
            while max_heap[0][1] < r - k + 1:
                heapq.heappop(max_heap)

            if r >= k - 1:
                result.append(-max_heap[0][0])

        return result

            
        
