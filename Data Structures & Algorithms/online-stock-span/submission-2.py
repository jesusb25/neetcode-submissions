class StockSpanner:

    def __init__(self):
        self.prices = [] # always decrease
        self.days = 0
        

    def next(self, price: int) -> int:
        print(self.prices)
        self.days += 1

        # remove same prices days to avoid returning distances between two same price days
        while self.prices and self.prices[-1][0] <= price:
            self.prices.pop()
            
        self.prices.append([price, self.days])
        
        if len(self.prices) > 1:
            return self.days - self.prices[-2][1]
        return self.days
        
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)