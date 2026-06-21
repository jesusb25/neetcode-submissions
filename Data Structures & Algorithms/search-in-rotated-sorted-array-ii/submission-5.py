class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        
        # search sub arrays as sorted
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            
            if nums[mid] == nums[left] == nums[right]:
                right -= 1
                left += 1
            
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1


            else:
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
