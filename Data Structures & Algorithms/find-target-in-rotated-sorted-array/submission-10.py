class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find min in array
        # then search in the array
        # [3,4,5,6,1,2]
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
        
        if nums[right] <= target and target <= nums[len(nums) - 1]:
            left = right
            right = len(nums) - 1
        else:
            left = 0
            right -= 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1


        