class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        MOD = 10**9 + 7
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
                continue
            res = (res + pow(2, right - left, MOD)) % MOD
            left += 1

        return res