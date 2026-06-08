class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        picked = set()

        def dfs(perm):
            if len(perm) == len(nums):
                result.append(perm[:])
                return

            for i in range(len(nums)):
                if i not in picked:
                    picked.add(i)
                    perm.append(nums[i])
                    dfs(perm)
                    picked.remove(i)
                    perm.pop()

                
            
        dfs([])
        return result
        