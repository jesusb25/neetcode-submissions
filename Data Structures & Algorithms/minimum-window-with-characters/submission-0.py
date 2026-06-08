class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # slide right further until complete 
        # slide left until hit a string in it
        original = [0] * 52
        shortest = s

        l, r = 0, 0

        count = defaultdict(int)
        for char in t:
            count[char] += 1
        
        countS = defaultdict(int)
        for char in s:
            countS[char] += 1
        
        for char in count:
            if countS[char] < count[char]:
                return ""
        
        while r < len(s):
            while max(count.values()) > 0 and r < len(s):
                count[s[r]] -= 1
                r += 1
            while max(count.values()) < 1 and l < r:
                if r - l < len(shortest):
                    shortest = s[l : r]
                count[s[l]] += 1
                l += 1
        return shortest
            
