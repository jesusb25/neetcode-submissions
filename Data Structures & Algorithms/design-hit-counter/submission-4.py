class HitCounter:

    def __init__(self):
        # queue of timestamps 
        self.q = deque()
        self.hashmap = {}
        

    def hit(self, timestamp: int) -> None:
        self.getHits(timestamp)

        if timestamp not in self.hashmap:  
            self.q.append(timestamp)
            self.hashmap[timestamp] = 1
        else: 
            self.hashmap[timestamp] += 1
 
        

    def getHits(self, timestamp: int) -> int:
        # remove out of time hits
        while self.q and self.q[0] <= timestamp - 300:
            time = self.q.popleft()
            del self.hashmap[time]
                
        print(self.hashmap)
        return sum(self.hashmap.values())
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
