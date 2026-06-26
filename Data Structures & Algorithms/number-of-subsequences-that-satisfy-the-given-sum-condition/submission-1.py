class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        mod = 10**9 + 7
        nums.sort()
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                # Add all valid subsequences for this minimum value
                res = (res + pow(2, right - left, mod)) % mod
                left += 1
                
        return res