class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # dq with indices
        # dq is always decreasing in vals

        result = []
        dq = deque()
        left = 0

        for r, num in enumerate(nums):
            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(r)
            
            while dq[0] <= r - k:
                dq.popleft()

            if r >= k - 1:
                result.append(nums[dq[0]])
        return result
            

            
        
