class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        prev = -1
        total_right = len(nums)

        while i < len(nums):
            if prev < total_right <= nums[i]:
                return total_right

            prev = nums[i]
            i += 1
            total_right = len(nums) - i

        return -1