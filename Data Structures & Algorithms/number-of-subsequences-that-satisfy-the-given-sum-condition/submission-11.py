class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()

        left = 0
        right = len(nums) - 1

        mod = 10**9 + 7

        while left <= right:
            if nums[right] + nums[left] > target:
                right -= 1
            else:
                res = res % mod + 2**(right - left) % mod
                left += 1
        return res