class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # return min of all paths at specific change unless impossible return -1
        if amount == 0:
            return 0
        memo = {}

        def dfs(target):
            if target == 0:
                return 0
            
            if target < 0:
                return -1

            if target in memo:
                return memo[target]

            # try all next steps, mark this as fail if all options were messed up
            best = None
            for coin in coins:
                count = dfs(target - coin)
                if count != -1 and (best == None or best > count):
                    best = count
                
            if best != None:
                memo[target] = 1 + best
                return 1 + best
            else:
                memo[target] = -1
                return -1

        dfs(amount)
        return memo[amount]
            



