class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break
            
            if i != 0 and num == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = num + nums[r] + nums[l]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([num, nums[r], nums[l]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res