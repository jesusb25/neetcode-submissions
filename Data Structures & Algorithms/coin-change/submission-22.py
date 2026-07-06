class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen = {}
        # coins.sort(reverse = True)

        def dfs(curr, total):
            if total == amount:
                return curr
            
            if total > amount:
                return -1
            
            if total in seen and seen[total] <= curr:
                return -1

            res = float('inf')
            
            for coin in coins:
                needed = dfs(curr + 1, total + coin)
                if needed != -1:
                    res = min(res, needed)
            
            seen[total] = curr
            return res if res < float('inf') else -1
        return dfs(0, 0)
