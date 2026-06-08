class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 
        sell = 1
        bestProfit = 0


        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit > bestProfit:
                bestProfit = profit
            if prices[buy] >= prices[sell]:
                buy = sell
                sell += 1
            else:
                sell += 1
        return bestProfit

        