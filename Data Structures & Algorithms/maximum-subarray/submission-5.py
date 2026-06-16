class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = -float('inf')
        res = -float('inf')
        for i in range(len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            res = max(res, currSum)
        return res