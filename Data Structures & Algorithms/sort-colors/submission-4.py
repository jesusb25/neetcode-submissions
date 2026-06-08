class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointers
        # move left to right, switch them as needed
        start = 0
        end = len(nums) - 1
        i = start
        while i < len(nums):
            if nums[i] == 0 and i >= start:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
                continue
            if nums[i] == 2 and i <= end:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
                continue
            i += 1
            if start > end:
                break

        return nums
            


        