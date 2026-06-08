class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest = 1

        numSet = set(nums)
        first = min(nums)
        
        for num in numSet:
            if num - 1 not in numSet:
                current = 1
                while num + 1 in numSet:
                    num += 1
                    current += 1
                longest = max(longest, current)
        return longest
