class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = 0
        w = 0


        while r < len(nums):
            # start count for target
            count = 0
            target = nums[r]

            # count target occ
            while r < len(nums) and nums[r] == target:
                r += 1
                count += 1
            
            # write at most 2
            for i in range(min(count, 2)):
                nums[w] = target
                w += 1
        return w
