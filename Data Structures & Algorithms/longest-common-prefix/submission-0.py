class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        res = strs[0]
        for i in range(len(res)):
            if res[i] != strs[-1][i]:
                return res[:i]
            
        return res