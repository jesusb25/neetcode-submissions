class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)

        for word in strs:
            wordKey = tuple(sorted(word))
            groupings[wordKey].append(word)
        
        return list(groupings.values())
        