class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for word in strs:
            length = len(word)
            result.append(str(length) + "#" + word)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []

        left = 0
        right = 1
        while right < len(s):
            while s[right] != "#":
                right += 1
            length = int(s[left : right])
            start = right + 1
            left = start + length
            right = left
            result.append(s[start : start + length])
        return result