class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # O(m * n)
        # O(1)
        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] and r > 0:
                    matrix[r][c] += matrix[r - 1][c]


            heights = sorted(matrix[r], reverse = True)
            for c in range(COLS):
                res = max(res, heights[c] * (c + 1))
        return res