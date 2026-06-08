class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(total, index):
            # if met target req
            if total == 0:
                result.append(subset.copy())
            
            # if dead end
            if total <= 0 or index == len(nums):
                return

            # include
            subset.append(nums[index])
            dfs(total - nums[index], index)

            # dont include
            subset.pop()
            dfs(total, index + 1)


        # kick off exploration 
        dfs(target, 0)
        return result