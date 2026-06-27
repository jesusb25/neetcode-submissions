class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        memo = set()
        
        def dfs(s1, s2, index):
            if index == len(nums):
                return s1 == s2
            
            if (s1, s2, index) in memo:
                return False
            
            # include in s1
            if dfs(s1 + nums[index], s2, index + 1):
                return True

            # inlcude in s2
            if dfs(s1, s2 + nums[index], index + 1):
                return True
            
            memo.add((s1, s2, index))
            memo.add((s2, s1, index))


            return False
        
        return dfs(0, 0, 0)

