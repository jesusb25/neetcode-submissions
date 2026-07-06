class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if not words or not words[0]:
            return True
        ROWS = len(words)
        for i in range(ROWS):
            for j in range(len(words[i])):
                # if j off rows or i off word
                if j >= ROWS or i >= len(words[j]):
                    return False
                if words[i][j] != words[j][i]:
                    return False
        return True