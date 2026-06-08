class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode by using num and delimiters
        # strs = ["Hello","World"]
        # "5#Hello5#World"
        result = []
        # encode words in array
        for word in strs:
            length = len(word)
            result.append(f"{length}#{word}")


        # return join words
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        # "5#Hello5#World"
        #    l 
        # start result
        # use two pointers to chunk words
        left = right = 0
        result = []

        while left < len(s):
            # find delimeter
            while s[right] != "#":
                right += 1

            length = int(s[left : right])

            # start of word
            left = right + 1
            result.append(s[left : left + length])
            # first char after word, possibly end of string
            left = right = left + length

        return result

