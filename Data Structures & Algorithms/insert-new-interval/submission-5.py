class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        new_start, new_end = newInterval

        # add anything before
        while i < len(intervals) and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1
        
        # merge anything with
        while i < len(intervals) and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        res.append([new_start, new_end])

        # add anything after
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res



