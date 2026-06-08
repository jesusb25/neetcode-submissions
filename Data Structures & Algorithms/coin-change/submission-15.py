from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        queue = deque([amount])
        memo = {amount}
        steps = 0
        
        while queue:
            steps += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                for coin in coins:
                    next_amount = curr - coin
                    if next_amount == 0:
                        return steps
                    if next_amount > 0 and next_amount not in memo:
                        memo.add(next_amount)
                        queue.append(next_amount)
        
        return -1
