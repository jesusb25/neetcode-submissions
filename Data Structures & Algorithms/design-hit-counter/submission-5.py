class HitCounter:

    def __init__(self):
        self.array = [0] * 300 # [most recent -> least recent]
        self.last_timestamp = 0


    def hit(self, timestamp: int) -> None:
        self.getHits(timestamp)
        self.array[0] += 1
        

        

    def getHits(self, timestamp: int) -> int:
        new_array = [0] * 300

        offset = timestamp - self.last_timestamp
        res = 0
        for i, count in enumerate(self.array):
            new_i = i + offset
            if new_i < len(new_array):
                new_array[new_i] = count
                res += count

        self.array = new_array
        self.last_timestamp = timestamp
        return res

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
