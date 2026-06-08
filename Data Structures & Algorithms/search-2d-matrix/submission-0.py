class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search the first numbers of each
        # 
        def binarySearch(nums):
            # binary search on nums return index of target
            left = 0
            right = len(nums) - 1

            while left <= right:
                middle = (left + right) // 2
                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            
            return -1


        left = 0
        right = len(matrix) - 1
        while left <= right:
            middle = (left + right) // 2
            if matrix[middle][0] <= target and target <= matrix[middle][len(matrix[0]) - 1]:
                return binarySearch(matrix[middle]) != -1
            elif matrix[middle][0] < target:
                left = middle + 1
            else:
                right = middle - 1


        return False