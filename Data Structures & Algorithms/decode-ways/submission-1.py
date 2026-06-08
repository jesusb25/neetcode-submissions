class Solution:
    def numDecodings(self, s: str) -> int:
        # 1 - 26 can decode into chars
        # dfs explore by taking 1 num at a time or attempting two nums at a time

        decodings = set([str(num) for num in range(10, 27)])
        memo = {}

        def dfs(index):
            if index in memo:
                return memo[index]

            if index == len(s):
                return 1
            
            if s[index] == "0":
                return 0
            
            total = dfs(index + 1)
            if s[index : index + 2] in decodings:
                total += dfs(index + 2)
            memo[index] = total
            return total

        return dfs(0)