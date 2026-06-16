class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 3 2 3 = 8
        res = 0
        for num in nums:
            res = num ^ res
        return res