class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # have = how many chars are met
        original = defaultdict(int)
        window = defaultdict(int)
        best_len = float("inf")
        best_start = 0
        l = 0

        # count original chars in dict
        for char in t:
            original[char] += 1
        have, need = 0, len(original.keys())
        

        for r, char in enumerate(s):
            # check if adding s[r] helps and if we met another need
            if char in original:
                window[char] += 1
                if window[char] == original[char]:
                    have += 1
            # contract window as much as possible
            while have == need and l <= r:
                if best_len > r - l + 1:
                    best_len = r - l + 1
                    best_start = l
                if s[l] in original:
                    if window[s[l]] == original[s[l]]:
                        have -= 1
                    window[s[l]] -= 1
                l += 1
        

        if best_len < float("inf"):
            return s[best_start : best_start + best_len]
        else:
            return ""