class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = 0
        w = 0


        while r < len(nums):
            count = 1
            target = nums[r]
            r += 1
            while r < len(nums) and nums[r] == target:
                r += 1
                count += 1
            
            for i in range(min(count, 2)):
                nums[w] = target
                w += 1
        return w
