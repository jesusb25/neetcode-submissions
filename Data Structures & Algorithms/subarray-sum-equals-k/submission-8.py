class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0:1}
        prefix = 0
        res = 0

        for num in nums:
            prefix += num
            # k = prefix - diff
            diff = prefix - k
            res += counts.get(diff, 0)
            counts[prefix] = counts.get(prefix, 0) + 1
        
        return res

