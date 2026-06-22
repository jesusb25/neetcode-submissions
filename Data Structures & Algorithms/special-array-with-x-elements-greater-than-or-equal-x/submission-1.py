class Solution:
    def specialArray(self, nums: List[int]) -> int:
        left = 0
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2

            more = 0

            for num in nums:
                if num >= mid:
                    more += 1
            
            if more == mid:
                return mid
            elif more < mid:
                right = mid - 1
            else:
                left = mid + 1
                
        return -1
