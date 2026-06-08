class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best_area = 0

        while left != right:
            curr_area = (right - left) * min(heights[left], heights[right])
            best_area = max(best_area, curr_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return best_area