class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # left to right
        # top to bottom



        # only do left to right if top is not bottom and right is not left



        result = []

        left, top = 0, 0
        right, bottom = len(matrix[0]) - 1, len(matrix) - 1

        while left <= right and top <= bottom:

            # left to right inclusive
            for i in range(left, right + 1):
                result.append(matrix[top][i])

            # top + 1 to bottom inclusive
            for i in range(top + 1, bottom + 1):
                result.append(matrix[i][right])
            # if left to right not done yet, run it
            # if bottom to top not run yet, run it
            if top != bottom:
                for i in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom][i])

            if left != right:
                for i in range(bottom - 1, top, -1):
                    result.append(matrix[i][left])
            right -= 1
            left += 1
            bottom -= 1
            top += 1


           


        return result