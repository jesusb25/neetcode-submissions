class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i, prev):
            if i == len(nums) or (i, prev) in memo:
                return memo.get((i, prev), 0)

            res = 0
            if prev < nums[i]:
                res = max(res, 1 + dfs(i + 1, nums[i]))
            res = max(res, dfs(i + 1, prev))
            memo[(i, prev)] = res
            return res

        return dfs(0, -float('inf'))
            
            
