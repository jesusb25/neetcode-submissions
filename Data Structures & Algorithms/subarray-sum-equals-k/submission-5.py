class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        curr = 0
        res = 0

        for num in nums:
            prefix[curr] += 1
            # curr + ? = k
            # ? = k - curr
            curr += num
            res += prefix[curr - k]
        return res