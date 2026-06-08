class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # edge cases: no answer, bad input, nums empty or none, target is not num
        # nums
        # target
        # return i and j 
        # i != j and nums[i] + nums[j] == target
        # go thorugh and collect the nums in a set
        

        # create seen dict
        seen = {}

        # go through nums
        # if compliment has been seen, return current index and seen index
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            
            seen[num] = i
        # what shoudl we return if no answer
        return [-1, -1] 
