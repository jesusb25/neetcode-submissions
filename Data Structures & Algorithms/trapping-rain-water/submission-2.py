class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        # highest from left highest from right 
        prefix = []
        result = []
        pre = 0
        for h in height:
            prefix.append(pre)
            pre = max(pre, h)
        
        post = 0
        for i in range(len(height) - 1, -1, -1):
            bounding = min(prefix[i], post)
            result.append(max(0, bounding - height[i]))
            post = max(post, height[i])            

        return sum(result)
