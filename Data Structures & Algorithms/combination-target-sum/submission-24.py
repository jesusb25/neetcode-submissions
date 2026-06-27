class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        memo = set() # index, total

        def dfs(index, total):
            if total == target:
                res.append(path[::])
                return 

            if total > target or index == len(nums) or (index, total) in memo:
                memo.add((index, total))
                return 
            
            # include
            path.append(nums[index])
            dfs(index, total + nums[index])
            path.pop()

            # exclude
            dfs(index + 1, total)

            
        dfs(0, 0)
        return res
