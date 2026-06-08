class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        result = nums[-1]

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if result > nums[middle]:
                result = nums[middle]
                right = middle - 1
            else:
                left = middle + 1
        return result
