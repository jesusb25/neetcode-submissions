class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        intervals.sort()
         
        res.append(intervals[0])

        for start, end in intervals[1:]:
            prev_start, prev_end = res[-1]
            if start <= prev_end:
                prev_start = min(start, prev_start)
                prev_end = max(prev_end, end)
            
                res[-1] = [prev_start, prev_end]
            else:
                res.append([start, end])
        return res