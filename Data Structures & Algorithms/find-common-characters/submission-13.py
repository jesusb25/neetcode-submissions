class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        common = Counter(words[0])

        for word in words:
            common &= Counter(word)
        
        res = []
        for key, count in common.items():
            res += [key] * count
        return res