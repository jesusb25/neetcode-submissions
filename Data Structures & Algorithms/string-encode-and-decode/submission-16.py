class Solution:

    def encode(self, strs: List[str]) -> str:
        # 8#strength6#monkey ...

        result = ""
        for word in strs:
            word_length = len(word)
            result += str(word_length) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []

        left = 0
        right = 0
        while left < len(s):

            while s[right] != '#':
                right += 1
            
            length = s[left:right]

            left = right + 1
            right = left + int(length)
            result.append(s[left : right])
            left = right
        return result
            

