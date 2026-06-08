class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encoded.append(str(len(word)) + "#" + word)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        result = []

        
        right = 0

        # 5#hello5#world
        while right < len(s):
            left = right
            while s[right] != "#":
                right += 1
            length = int(s[left : right])
            left = right + 1
            right = left + length
            result.append(s[left : right])
        return result

