class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        memo = {}
        
        def dfs(target):
            if target == 0:
                return 0
            
            if target in memo:
                return memo[target]

            res = float('inf')
            for coin in coins:
                if (target - coin) >= 0:
                    res = min(res, 1 + dfs(target - coin))
            
            memo[target] = res
            return res
        best = dfs(amount)
        if best > amount:
            return -1
        return memo[amount]







                    
