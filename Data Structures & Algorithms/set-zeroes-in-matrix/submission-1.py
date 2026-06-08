class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # go thorugh entire array, row by row col by col
        # mark rows that need to be changed with float
        ROWS = len(matrix)
        COLS = len(matrix[0])
        if not matrix:
            return 

        def markNone(row, col):
            # mark entire row if not 0
            for i in range(len(matrix[0])):
                if matrix[row][i] == 0:
                    continue
                
                matrix[row][i] = None

            # mark entire col if not 0
            for i in range(len(matrix)):
                if matrix[i][col] == 0:
                    continue
                
                matrix[i][col] = None

        # if element is 0, mark entire row and column
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    markNone(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == None:
                    matrix[r][c] = 0

        # return matrix
        
        