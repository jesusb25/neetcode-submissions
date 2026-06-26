class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ctr = Counter(text)
        return min(ctr["b"], ctr['a'], ctr['l'] // 2, ctr['o'] // 2, ctr['n'])