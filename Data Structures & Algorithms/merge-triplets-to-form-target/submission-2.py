class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # if max so far
        largest = max(target)
        curr = [-float("inf"), -float("inf"), -float("inf")]
        for triplet in triplets:
            if max(triplet) > largest:
                continue
            
            for i in range(len(curr)):
                curr[i] = max(curr[i], triplet[i])
            
            if curr == target:
                return True
        return False
            
