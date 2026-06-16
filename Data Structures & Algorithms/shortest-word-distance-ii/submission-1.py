class WordDistance:

    def __init__(self, wordsDict: List[str]):
        # track distance by index
        # multiple copies of each word
        # turn everything into node graphs
        # bfs from each node ? 
        # hashmap word to index
        self.locs = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.locs[word].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        res = float('inf')
        i1 = i2 = 0
        locs1 = self.locs[word1]
        locs2 = self.locs[word2]

        while i1 < len(locs1) and i2 < len(locs2):
            res = min(res, abs(locs1[i1] - locs2[i2]))
            if locs1[i1] < locs2[i2]:
                i1 += 1
            else:
                i2 += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
