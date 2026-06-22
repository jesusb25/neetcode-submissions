class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        memo = set()

        candidates.sort()
        path = []
        res = []

        def dfs(curr, i):
            if curr == target:
                res.append(path[:])
                return
            
            if curr > target or i == len(candidates):
                return
            
            # include
            path.append(candidates[i])
            dfs(curr + candidates[i], i + 1)
            path.pop()

            # exclude next
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(curr, i + 1)

        dfs(0, 0)
        return res
