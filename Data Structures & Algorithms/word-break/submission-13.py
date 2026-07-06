class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        seen = set()

        def dfs(curr):
            if not curr:
                return True
            
            if curr in seen:
                return False
            
            for i in range(len(curr) + 1):
                if curr[:i] in words and dfs(curr[i:]):
                    return True
            
            seen.add(curr)
            return False
        
        return dfs(s)