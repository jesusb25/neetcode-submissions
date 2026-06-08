class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        failed_suffix = set() # store failed suffix to avoid rabbit holes

        def dfs(i):
            if i >= len(s):
                return True
            
            if i in failed_suffix:
                return False
            
            for word in wordDict:
                if word == s[i:i + len(word)]:
                    if dfs(i + len(word)):
                        return True       
            failed_suffix.add(i + len(word))
            return False

        return dfs(0)



