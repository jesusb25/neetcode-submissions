class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        
        ROWS = len(boxGrid)
        COLS = len(boxGrid[0])

        for r in range(ROWS):
            i = COLS - 1

            for c in range(COLS - 1, -1, -1):
                if boxGrid[r][c] == "#":
                    boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c]
                    i -= 1

                elif boxGrid[r][c] == "*":
                    i = c - 1
                
        res = []
        for c in range(COLS):
            row = []
            for r in reversed(range(ROWS)):
                row.append(boxGrid[r][c])
            res.append(row)
        return res


                
