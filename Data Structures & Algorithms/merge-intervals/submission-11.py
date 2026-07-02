class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = defaultdict(int)

        for start, end in intervals:
            events[start] += 1
            events[end] -= 1
        
        res = []
        interval = []
        active = 0
        for i in sorted(events):
            if not interval:
                interval.append(i)
            active += events[i]
            if active == 0:
                interval.append(i)
                res.append(interval)
                interval = []
        return res