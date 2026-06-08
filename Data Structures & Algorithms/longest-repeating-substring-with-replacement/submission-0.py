class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AAABABB
        counts = defaultdict(int)
        left = 0
        longest = 0
        maxF = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            maxF = max(maxF, counts[s[right]])
            
            if (right - left + 1) - maxF > k:
                counts[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
