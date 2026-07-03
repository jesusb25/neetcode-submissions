class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            seen = set()
            added_to_res = set()
            for j in range(i + 1, len(nums)):
                # seen + num == target
                num = nums[j]
                if target - num in seen and num not in added_to_res:
                    res.append([nums[i], target - num, num])
                    added_to_res.add(num)
                seen.add(num)

           
        return res
