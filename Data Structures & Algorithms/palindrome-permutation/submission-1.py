class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = Counter(s)

        odds = sum(1 if val % 2 != 0 else 0 for val in counts.values())
        return odds <= 1