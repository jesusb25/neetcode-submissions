class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i, num in enumerate(nums):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            
            target = -num
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[right] + nums[left]
                if total == target:
                    result.append([num, nums[left], nums[right]])
                    curr_left, curr_right = nums[left], nums[right]
                    while left != n and nums[left] == curr_left:
                        left += 1
                    while right != - 1 and nums[right] == curr_right:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return result


