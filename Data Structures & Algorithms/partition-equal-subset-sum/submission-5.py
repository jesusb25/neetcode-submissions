class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        memo = set()

        def dfs(i, target):
            if i >= len(nums):
                return target == 0
            if target < 0 or (i, target) in memo:
                return False


            res = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            memo.add((i, target))
            return res

        return dfs(0, sum(nums) // 2)