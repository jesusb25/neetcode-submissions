class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # hold [height, index]
        best_area = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                prev_height, prev_index = stack.pop()
                best_area = max(best_area, prev_height * (i - prev_index))
                start = prev_index
            
            stack.append([height, start])

        while stack:
            prev_height, prev_index = stack.pop()
            best_area = max(best_area, prev_height * (len(heights) - prev_index))
        return best_area




        