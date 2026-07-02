class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = defaultdict(int)

        for start, end in intervals:
            events[start] += 1
            events[end] -= 1
        
        res = []
        start = None
        active = 0
        for i in sorted(events):
            if start is None:
                start = i

            active += events[i] 

            if active == 0:
                res.append([start, i])
                start = None
        return res
