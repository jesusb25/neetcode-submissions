class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        # 1. start anagram dict
        anagrams = defaultdict(list)
        # 2. get character count in array * 26
        for word in strs:
            count = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1
            # 3. group like anagrams
            anagrams[tuple(count)].append(word)
        
        # 4. return anagram groupings as list of lists
        # O(n) O(n)
        return list(anagrams.values())