class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap? 
        # bucket sort
        # count freq
        count = defaultdict(int)
        bucket_count = 0
        for num in nums:
            count[num] += 1
            bucket_count = max(bucket_count, count[num])
        
        # bucket sort by counts count == index
        buckets = [[] for i in range(bucket_count + 1)]
        for num, count in count.items():
            buckets[count].append(num)

        # work backwards in buckets
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            # return top k
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
                
        return result