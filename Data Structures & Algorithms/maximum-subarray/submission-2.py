class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = [0]
        total = 0

        for num in nums:
            total += num
            prefix.append(total)
    
        res = sum(nums)
        # min from left
        # max from right
        min_left = float("inf")
        min_arr = []

        for i, num in enumerate(prefix):
            min_arr.append(min_left)
            min_left = min(min_left, num)

        for i in range(len(prefix) - 1, -1, -1):
            res = max(res, prefix[i] - min_arr[i])
        return res
