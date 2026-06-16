class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = []

        for i in range(len(nums)):
            if i == 0:
                sums.append(nums[i])
            else:
                sums.append(max(nums[i], nums[i] + sums[i - 1]))
        return max(sums)