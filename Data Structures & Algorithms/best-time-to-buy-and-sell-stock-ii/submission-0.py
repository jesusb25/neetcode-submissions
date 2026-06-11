class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # only hold one stock a day
        # buy and sell over and over
        # buy as low as you can, then sell day before drop where youll buy again
        left = 0
        right = 1
        profit = 0
        # [7,1,5,3,6,4]
        #    l   r     
        while right < len(prices):
            # if no point of buying move left
            if prices[left] > prices[right]:
                left = right
                right += 1
            else:    
                while right + 1 < len(prices) and prices[right] < prices[right + 1]:
                    right += 1
                profit += prices[right] - prices[left]
                left = right
                right += 1
        return profit
            

        
        