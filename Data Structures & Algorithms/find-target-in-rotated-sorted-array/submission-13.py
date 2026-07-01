class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        left = 0
        right = len(nums) - 1


        # left side is sorted
        while left <= right:
            mid = (left + right) // 2

            
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                # find side to visit
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # right side is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # find side to visit
                else:
                    right = mid - 1
  
        return -1

