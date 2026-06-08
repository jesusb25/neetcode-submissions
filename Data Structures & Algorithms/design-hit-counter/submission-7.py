class HitCounter:

    def __init__(self):
        self.hits = collections.deque()  # deque of (timestamp, count)

    def hit(self, timestamp: int) -> None:
        self.getHits(timestamp)
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1] = (timestamp, self.hits[-1][1] + 1)
        else:
            self.hits.append((timestamp, 1))

    def getHits(self, timestamp: int) -> int:
        while self.hits and timestamp - self.hits[0][0] >= 300:
            self.hits.popleft()

        return sum(count for _, count in self.hits)