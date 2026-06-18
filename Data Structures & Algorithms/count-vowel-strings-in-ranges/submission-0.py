class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        counts = [0]
        vowels = set(["a", "e", "i", "o", "u"])
        # [1, 2, 3]
        # [1, 3, 6]
        prefixSum = 0
        for word in words:
            if word and word[0] in vowels and word[-1] in vowels:
                prefixSum += 1
            counts.append(prefixSum)
        
        res = []
        for start, end in queries:
            res.append(counts[end + 1] - counts[start])
        return res
            