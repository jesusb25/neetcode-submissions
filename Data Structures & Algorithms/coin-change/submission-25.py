class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(left):
            if left == 0:
                return 0
            if left in memo:
                return memo[left]

            res = 1e9
            for coin in coins:
                if left - coin >= 0:
                    res = min(res, 1 + dfs(left - coin))

            memo[left] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins