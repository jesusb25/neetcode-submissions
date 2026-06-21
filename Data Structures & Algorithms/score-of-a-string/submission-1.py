class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        for i, char in enumerate(s):
            if i == 0:
                continue
            res += abs(ord(char) - ord(s[i - 1]))
        return res