class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        
        res = 0
        for lst in indices.values():
            n = len(lst)
            if n == 1:
                continue
            res += n * (n - 1) // 2
        return res
