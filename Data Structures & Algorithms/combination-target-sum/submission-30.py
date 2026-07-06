class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def dfs(index, total):
            if total == target:
                res.append(path[::])
                return
            
            if index == len(nums) or total > target:
                return 
            
            if nums[index] != nums[index - 1]:
                # include
                path.append(nums[index])
                dfs(index, total + nums[index])
                path.pop()

            # exclude
            dfs(index + 1, total)

            
        dfs(0, 0)
        return res