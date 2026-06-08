class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        questions:
        can we assume no spaces
        should we ignore spaces
        can we assume all lowercase
        what if both empty?
        what if one empty?
        '''
        # validate both exists
        if not s or not t:
            return s == t
        
        if len(s) != len(t):
            return False

        
        # count chars in each and compare counts
        countS = defaultdict(int)
        countT = defaultdict(int)

        for charS, charT in zip(list(s), list(t)):
            countS[charS] += 1
            countT[charT] += 1
        return countS == countT
        