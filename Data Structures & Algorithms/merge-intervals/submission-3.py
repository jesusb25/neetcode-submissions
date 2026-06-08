class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # go through intervals, if overlap exists with most recent update end
        # otherwise add to result regardless
        if not intervals:
            return []
        intervals.sort()
        result = []

        for start, end in intervals:
            
            prev_end = result[-1][1] if result else -float('inf')
            if start <= prev_end:
                result[-1][1] = max(end, prev_end)
            else: 
                result.append([start, end])
        return result

            
