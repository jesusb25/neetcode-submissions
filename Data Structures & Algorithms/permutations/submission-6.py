class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        picked = [False] * len(nums)

        def dfs(perm):
            if len(perm) == len(picked):
                result.append(perm[:])
                return

            for i in range(len(picked)):
                if not picked[i]:
                    picked[i] = True
                    perm.append(nums[i])
                    dfs(perm)
                    picked[i] = False
                    perm.pop()

                
            
        dfs([])
        return result
        