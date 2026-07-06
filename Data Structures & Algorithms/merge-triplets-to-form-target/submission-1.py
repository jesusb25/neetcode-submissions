class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # if max so far
        curr = [-float("inf"), -float("inf"), -float("inf")]
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            for i in range(len(curr)):
                curr[i] = max(curr[i], triplet[i])
            
            if curr == target:
                return True
        return False
            
