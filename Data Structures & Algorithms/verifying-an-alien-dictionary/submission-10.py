class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {char : i for i, char in enumerate(order)}

        def compare(word):
            return [orderMap[c] for c in word]
        
        return words == sorted(words, key = compare)