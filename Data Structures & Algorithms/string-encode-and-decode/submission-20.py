class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encoded.append(str(len(word)) + "#" + word)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        result = []

        left = 0
        right = 1

        # 5#hello5#world
        while left < right and right < len(s):
            while s[right] != "#":
                right += 1
            length = int(s[left:right])
            right += 1
            result.append(s[right : right + length])
            left = right + length
            right = left + 1
        return result

