class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        nums = sorted(nums)

        for i in range(len(nums)):
            target = -nums[i]
            # two sum with rest of array
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1 
        return list(result)