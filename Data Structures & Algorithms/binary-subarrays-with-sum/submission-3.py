class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = 0
        counts = defaultdict(int)
        counts[0] = 1

        res = 0
        for num in nums:
            prefix += num
            res += counts[prefix - goal]
            counts[prefix] += 1
        return res