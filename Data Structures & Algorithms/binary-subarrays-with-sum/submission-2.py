class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        count = defaultdict(int)
        count[0] = 1
        res = 0

        prefix = 0
        for num in nums:
            prefix += num
            res += count[prefix - goal]
            count[prefix] += 1
        return res