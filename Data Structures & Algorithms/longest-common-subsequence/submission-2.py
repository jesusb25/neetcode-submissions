class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(index1, index2):
            if index1 == len(text1) or index2 == len(text2):
                return 0

            if (index1, index2) in memo:
                return memo[(index1, index2)]
            
            # three options match, skip 1, skip 2
            res = 0
            if text1[index1] == text2[index2]:
                res = max(res, 1 + dfs(index1 + 1, index2 + 1))
            
            res = max(res, dfs(index1 + 1, index2), dfs(index1, index2 + 1))
            memo[(index1, index2)] = res
            return res
        
        return dfs(0, 0)
