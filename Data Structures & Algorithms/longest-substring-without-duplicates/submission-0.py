class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # zyxyx
        if len(s) < 2:
            return len(s)
        seen = set()
        seen.add(s[0])
        left = 0
        right = 1
        longest = 1
        while left < right and right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            right += 1
            longest = max(longest, right - left)
        return longest


        

