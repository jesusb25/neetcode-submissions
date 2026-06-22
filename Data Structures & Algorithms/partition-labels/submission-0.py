class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indices = defaultdict(list)
        for i, char in enumerate(s):
            indices[char].append(i)
        
        intervals = []
        for interval in indices.values():
            start = interval[0]
            end = interval[-1]
            intervals.append([start, end])
        


        # start end then merge intervals and return lengths
        merged = []
        for start, end in intervals:
            if merged and merged[-1][1] >= start:
                merged[-1][1] = max(merged[-1][1], end)
                merged[-1][0] = min(start, merged[-1][0])
            else:
                merged.append([start,end])
        res = []
        for start, end in merged:
            res.append(end - start + 1)
        return res


        