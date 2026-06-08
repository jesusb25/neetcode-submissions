class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        l,r = 0,0
        maxf = 0
        res=0

        while r < len(s):
            
            letter = s[r]
            seen[letter] +=1
            maxf = max(maxf, seen[letter])
            while (r - l + 1) - maxf >k:
                seen[s[l]] -=1
                l += 1
            
            res=max(res,r - l + 1)
            r += 1
        return res