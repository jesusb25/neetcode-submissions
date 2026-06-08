class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        # highest from left highest from right 
        prefix = []
        postfix = [0] * len(height)
        result = []
        pre = 0
        for h in height:
            prefix.append(pre)
            pre = max(pre, h)
        
        post = 0
        for i in range(len(height) - 1, -1, -1):
            postfix[i] = post
            post = max(post, height[i])
        
        for i in range(len(height)):
            bounding = min(prefix[i], postfix[i])
            result.append(max(0, bounding - height[i]))

        return sum(result)
