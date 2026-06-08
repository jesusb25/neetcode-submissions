class TimeMap:

    def __init__(self):
        # search at time stamp
        # binary search times
        # dict key : [[value, timestamp], ...]
        # timestamp at such time
        # return "" when earliest time stamp is after get time stamp
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or timestamp < self.store[key][0][1]:
            return ""
        
        values = self.store[key]

        left = 0
        right = len(values) - 1
        closest = values[0]
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] > timestamp:
                right = middle - 1
            else:
                closest = values[middle][0]
                left = middle + 1
        
        return closest

        
