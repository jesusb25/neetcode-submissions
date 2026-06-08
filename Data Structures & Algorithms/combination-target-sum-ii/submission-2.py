class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        subset = []
        
        def dfs(index, total):
            if total == 0:
                result.append(subset.copy())
                return
            
            if total < 0 or index == len(candidates):
                return
            
            subset.append(candidates[index])
            dfs(index + 1, total - candidates[index])

            subset.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            
            dfs(index + 1, total)

        dfs(0, target)

        return result

