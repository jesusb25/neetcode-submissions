class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(index, total):
            if index == len(nums):
                if total == target:
                    res.append(path[::])
                return
            
            if total > target:
                return
            # include and keep going
            path.append(nums[index])
            dfs(index, total + nums[index])
            path.pop()

            # exclude
            dfs(index + 1, total)
        
        dfs(0, 0)
        return res
        
            
