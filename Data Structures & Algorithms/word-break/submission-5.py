class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # recursion dfs splitting where new word is made
        # otherwise return false
        wordDict = set(wordDict)
        memo_failed = set()

        def dfs(word_left):
            if not word_left:
                return True
            
            if word_left in memo_failed:
                return False
            
            for i in range(len(word_left) + 1):
                if word_left[:i] in wordDict:
                    if dfs(word_left[i:]):
                        return True
                    memo_failed.add(word_left[i:])
            return False

        return dfs(s)
            
