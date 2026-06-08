class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # sliding window array 26 chars
        # update sliding window based on length
        subArray = [0] * 26
        window = [0] * 26

        for i in range(len(s1)):
            subArray[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        if subArray == window:
            return True

        for right in range(len(s1), len(s2)):
            start = right - len(s1)
            window[ord(s2[start]) - ord('a')] -= 1
            window[ord(s2[right]) - ord('a')] += 1
            if subArray == window:
                return True
        return False



