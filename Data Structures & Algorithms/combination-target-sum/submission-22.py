class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []

        def dfs(index, remain):
            if remain == 0:
                res.append(combo.copy())
                return
            
            if remain < 0 or index == len(nums):
                return
            
            combo.append(nums[index])
            dfs(index, remain - nums[index])
            combo.pop()

            dfs(index + 1, remain)
        dfs(0, target)
        return res