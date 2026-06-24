class WordDistance:

    def __init__(self, wordsDict: List[str]):
        # distance between two strings
        self.locs = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.locs[word].append(i)

        

    def shortest(self, word1: str, word2: str) -> int:

        res = float('inf')
        locs1 = self.locs[word1]
        locs2 = self.locs[word2]
        left = right = 0

        while left < len(locs1) and right < len(locs2):
            res = min(res, abs(locs1[left] - locs2[right]))

            if locs1[left] < locs2[right]:
                left += 1
            else:
                right += 1
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
