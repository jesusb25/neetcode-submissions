class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        indices = {char: i for i, char in enumerate(order)}

        for i in range(1, len(words)):
            prev = words[i - 1]
            curr = words[i]
            prefix = True

            for i in range(min(len(prev), len(curr))):
                if indices[prev[i]] < indices[curr[i]]:
                    prefix = False
                    break
                elif indices[prev[i]] > indices[curr[i]]:
                    return False

                if prev[i] != curr[i]:
                    prefix = False
                
            if prefix and len(curr) < len(prev):
                return False

        return True
                