class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # buckets are capped by num elements
        # 2d list
        nums.sort()


        buckets = [[] for i in range(len(nums) + 1)]
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        for num, count in counts.items():
            buckets[count].append(num)
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result