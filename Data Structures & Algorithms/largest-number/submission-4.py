from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, num in enumerate(nums):
            nums[i] = str(num)

        
        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1
        
        nums.sort(key=cmp_to_key(compare))

        return "".join(nums) if nums[0][0] != "0" else "0"
        
        