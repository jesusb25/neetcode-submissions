class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)

        for word in strs:
            wordCount = [0] * 26
            for char in word:
                wordCount[ord(char) - ord('a')] += 1
            
            groupings[tuple(wordCount)].append(word)
        
        return list(groupings.values())
        