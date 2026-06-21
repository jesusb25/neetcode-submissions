class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = Counter()

        for word in words:
            counts += Counter(word)

        for key, count in counts.items():
            if count % len(words) != 0:
                return False
        return True