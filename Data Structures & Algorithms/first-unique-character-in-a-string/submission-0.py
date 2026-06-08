class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen_once = set()
        seen_twice = set()

        for char in s:
            if char in seen_once:
                seen_twice.add(char)
            seen_once.add(char)
        
        for i, char in enumerate(s):
            if char not in seen_twice:
                return i
        return -1
        

        