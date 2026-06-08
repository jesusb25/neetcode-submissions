class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def dfs(index):

            
            if index >= len(nums) - 1:
                return True
            
            for jump in range(nums[index], 0, -1):
                if dfs(index + jump):
                    return True
                
            return False
        return dfs(0)
