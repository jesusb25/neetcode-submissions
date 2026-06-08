class HitCounter:

    def __init__(self):
        # queue of timestamps 
        self.q = deque()
        

    def hit(self, timestamp: int) -> None:
        # remove out of time hits
        while self.q and self.q[0] < timestamp - 300:
            self.q.popleft()
        self.q.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        # remove out of time hits
        while self.q and self.q[0] <= timestamp - 300:
            self.q.popleft()
        return len(self.q)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
