from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = defaultdict(int)
        for char in t:
            need[char] += 1

        window = defaultdict(int)
        have, total_need = 0, len(need)  # distinct chars satisfied vs needed

        best_start, best_len = 0, float('inf')
        l = 0

        for r, char in enumerate(s):
            window[char] += 1

            # Check if this char's frequency in window satisfies need
            if char in need and window[char] == need[char]:
                have += 1

            # Contract window from left while all chars are satisfied
            while have == total_need:
                # Update best window
                if (r - l + 1) < best_len:
                    best_len = r - l + 1
                    best_start = l

                # Remove leftmost char and shrink
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        return s[best_start : best_start + best_len] if best_len != float('inf') else ""