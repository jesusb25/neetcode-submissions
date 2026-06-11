class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        curr = 0
        res = 0

        for num in nums:
            prefix[curr] += 1
            # curr sum - prev sum = k
            # curr - k = prev sum in prefix
            curr += num
            res += prefix[curr - k]
        return res