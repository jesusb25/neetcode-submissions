class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set of nums
        # if num - 1 not in nums: count
        # otherwise continue
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in nums:
                continue
            
            curr = num + 1
            while curr in nums:
                curr += 1
            longest = max(longest, curr - num)
        return longest