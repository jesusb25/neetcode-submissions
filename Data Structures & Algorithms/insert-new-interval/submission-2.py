class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # build result intervals

        # when new interval finds a space, update the previous end
        combined = []
        new_start, new_end = newInterval
        for curr_start, curr_end in intervals:
            if new_start < curr_start:
                combined.append(newInterval)
                new_start = float('inf')
            combined.append([curr_start, curr_end])
    
        if len(combined) == len(intervals):
            combined.append(newInterval)
        print(combined)
        # then merge all intervals as needed
        res = [combined[0]]
        for i, interval in enumerate(combined[1:]):
            curr_start, curr_end = interval
            prev_end = res[-1][1]
            if curr_start <= prev_end:
                res[-1][1] = max(res[-1][1], curr_end)
            else:
                res.append(interval)
        return res









        