class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if not digits:
            return []
        result = []
        path = []

        # if index is past last digit, add solution
        def dfs(index):
            if index == len(digits):
                result.append("".join(path))
                return

            # explore options using next char, join all chars for solution but build through path
            options = digit_map[digits[index]]

            for char in options:
                path.append(char)
                dfs(index + 1)
                path.pop()


        dfs(0)
        return result