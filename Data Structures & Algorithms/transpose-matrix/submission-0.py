class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        res = [[0] * ROWS for i in range(COLS)]
        for col in range(COLS):
            for row in range(ROWS):
                res[col][row] = matrix[row][col]
        return res
