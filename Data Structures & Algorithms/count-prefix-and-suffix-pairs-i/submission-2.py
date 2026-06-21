class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0

        def isPrefixAndSuffix(word1, word2):
            n = len(word1)
            return 1 if word1 == word2[:n] and word1 == word2[-n:] else 0
        
        for i, w1 in enumerate(words):
            for w2 in words[i + 1:]:
                res += isPrefixAndSuffix(w1, w2)
        return res