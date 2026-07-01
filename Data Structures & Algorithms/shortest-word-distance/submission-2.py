class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1 = -1
        i2 = -1
        res = float('inf')

        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i
            
            if word == word2:
                i2 = i
            
            if min(i1, i2) > -1:
                res = min(res, abs(i2 - i1))
        return res