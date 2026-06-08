class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(total, index):
            if total == 0:
                result.append(subset.copy())
            
            if total <= 0 or index == len(nums):
                return

            subset.append(nums[index])
            dfs(total - nums[index], index)

            subset.pop()
            dfs(total, index + 1)


            
        dfs(target, 0)
        return result