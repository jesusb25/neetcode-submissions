class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        result = []

        left = 0

        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            length = (int(s[left:right]))
            left = right + 1
            right = left + length
            result.append(s[left:right])
            left = right
        return result
        