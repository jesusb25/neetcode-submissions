class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        curr = 0
        for i, num in enumerate(nums):
            if curr == total - curr - num:
                return i

            curr += num 
        return -1