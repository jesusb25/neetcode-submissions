class TimeMap:

    def __init__(self):
        # time key value store
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        # binary search keep left time always move right
        if key not in self.hashmap:
            return ""
        entries = self.hashmap[key]
        if entries[0][0] > timestamp:
            return ""
        
        left = 0
        right = len(entries) - 1
        res = -1

        while left <= right:
            mid = (left + right) // 2
            if entries[mid][0] <= timestamp:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        
        return entries[res][1] if res != -1 else ""


