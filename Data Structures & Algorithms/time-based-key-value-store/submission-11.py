class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap or timestamp < self.hashmap[key][0][0]:
            return ""
        
        vals = self.hashmap[key]
        left = 0
        right = len(vals) - 1

        res = ""
        while left <= right:
            mid = (left + right) // 2

            if vals[mid][0] == timestamp:
                return vals[mid][1]
            elif vals[mid][0] > timestamp:
                right = mid - 1
            else:
                res = vals[mid][1]
                left = mid + 1
            
        return res

        

        
