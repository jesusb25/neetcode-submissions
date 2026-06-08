class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # dq with indices
        # dq is always decreasing in vals

        result = []
        dq = deque()

        for r, num in enumerate(nums):
            # pop values less than num since its now greatest
            while dq and nums[dq[-1]] < num:
                dq.pop()

            # add index of right most val
            dq.append(r)

            # remove out of range indices
            while dq[0] <= r - k:
                dq.popleft()

            # append max value so far
            if r >= k - 1:
                result.append(nums[dq[0]])
        return result
            

            
        
