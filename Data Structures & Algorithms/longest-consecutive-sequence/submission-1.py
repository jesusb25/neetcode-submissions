class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # Input: nums = [2,20,4,10,3,4,5]
        # Output: 4

        longest = 1
        for num in nums:
            if num + 1 in nums and num - 1 not in nums:
                curr_length = 1
                while num + curr_length in nums:
                    curr_length += 1
                longest = max(longest, curr_length)
                    

        return longest

        