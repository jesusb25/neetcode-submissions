class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            l = nums[mid - 1] if mid != 0 else -float('inf')
            r = nums[mid + 1] if mid + 1 != len(nums) else -float('inf')

            if l < nums[mid] > r:
                return mid
            
            if nums[mid] < r:
                left = mid + 1
                
            else:
                right = mid - 1

        return -1

