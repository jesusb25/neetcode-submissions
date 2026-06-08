class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        result = 0
        seen = set()

        left = 0
      

        # s="abcabcbb"
        # left = 0
        # right= 3
        for right in range(len(s)):
            if s[right] in seen:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1
            seen.add(s[right])
            result = max(result, right - left + 1)
        return result


        

