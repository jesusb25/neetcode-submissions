class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        events = []
        
        for start, end in intervals:
            events.append([start, 1])
            events.append([end, -1])

        active = 0
        events.sort(key=lambda e:[e[0], -e[1]])
        start = None
        for time, delta in events:
            # active inc or dec
            active += delta
            if start is None:
                start = time
            # event end
            elif active == 0:
                res.append([start, time])
                start = None
        return res


            
