class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for i in range(numRows)]

        # go from left to right iteration thorugh entire column
        i = 0
        down = True
        while i < len(s):
            if down:
                for row in range(numRows):
                    if i == len(s):
                        break
                    rows[row].append(s[i])
                    i += 1
            else:
                for row in range(numRows - 2, 0, -1):
                    if i == len(s):
                        break
                    rows[row].append(s[i])
                    i += 1
            down = not down
        
        # start step up until row 0
        # then combine each col for each row and then combine all rows
        res = ""
        for row in rows:
            res = res + "".join(row) 

        
        return res

