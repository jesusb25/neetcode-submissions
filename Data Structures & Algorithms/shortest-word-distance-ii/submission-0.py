class WordDistance:

    def __init__(self, wordsDict: List[str]):
        # track distance by index
        # multiple copies of each word
        # turn everything into node graphs
        # bfs from each node ? 
        # hashmap word to index
        self.words = wordsDict
        

    def shortest(self, word1: str, word2: str) -> int:
        i1 = i2 = -1
        res = float('inf')
        for i in range(len(self.words)):
            if self.words[i] == word1:
                i1 = i
            elif self.words[i] == word2:
                i2 = i
            
            if min(i1, i2) > -1:
                res = min(res, abs(i2 - i1))
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
